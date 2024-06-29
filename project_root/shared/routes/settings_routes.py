from flask import Blueprint, render_template, redirect, url_for, flash, request, send_file
from flask_login import login_required
from shared.models.database import db
from shared.models import Setting
from app.forms import SettingForm, BackupForm
import json
import io

settings_bp = Blueprint('settings', __name__)

@settings_bp.route('/settings', methods=['GET', 'POST'])
@login_required
def settings_page():
    form = SettingForm()
    backup_form = BackupForm()

    if form.validate_on_submit():
        ollama_url = Setting.query.filter_by(key='ollama_url').first()
        ollama_model = Setting.query.filter_by(key='ollama_model').first()

        if not ollama_url:
            ollama_url = Setting(key='ollama_url', value=form.ollama_url.data)
        else:
            ollama_url.value = form.ollama_url.data

        if not ollama_model:
            ollama_model = Setting(key='ollama_model', value=form.ollama_model.data)
        else:
            ollama_model.value = form.ollama_model.data

        db.session.add(ollama_url)
        db.session.add(ollama_model)
        db.session.commit()
        flash('Settings have been saved!', 'success')
        return redirect(url_for('settings.settings_page'))

    elif backup_form.submit_backup.data:
        settings = Setting.query.all()
        settings_data = {setting.key: setting.value for setting in settings}
        buffer = io.StringIO()
        json.dump(settings_data, buffer)
        buffer.seek(0)
        return send_file(io.BytesIO(buffer.getvalue().encode()), mimetype='application/json', as_attachment=True, attachment_filename='settings_backup.json')

    elif backup_form.submit_restore.data:
        file = request.files['file']
        if file:
            settings_data = json.load(file)
            for key, value in settings_data.items():
                setting = Setting.query.filter_by(key=key).first()
                if not setting:
                    setting = Setting(key=key, value=value)
                else:
                    setting.value = value
                db.session.add(setting)
            db.session.commit()
            flash('Settings have been restored!', 'success')
            return redirect(url_for('settings.settings_page'))

    ollama_url = Setting.query.filter_by(key='ollama_url').first()
    ollama_model = Setting.query.filter_by(key='ollama_model').first()

    if ollama_url:
        form.ollama_url.data = ollama_url.value
    if ollama_model:
        form.ollama_model.data = ollama_model.value

    return render_template('settings.html', form=form, backup_form=backup_form)
