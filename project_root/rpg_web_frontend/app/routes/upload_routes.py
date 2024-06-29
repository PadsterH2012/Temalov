from flask import Blueprint, render_template

upload_bp = Blueprint('upload', __name__)

@upload_bp.route('/upload', methods=['GET'])
def upload_page():
    return render_template('upload.html')
