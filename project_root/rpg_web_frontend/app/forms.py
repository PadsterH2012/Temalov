from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, PasswordField, FileField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, Email, ValidationError
from shared.models.entities import Player

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=150)])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        player = Player.query.filter_by(username=username.data).first()
        if player:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        player = Player.query.filter_by(email=email.data).first()
        if player:
            raise ValidationError('That email is taken. Please choose a different one.')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class SettingForm(FlaskForm):
    ollama_url = StringField('Ollama URL', validators=[DataRequired(), Length(max=200)])
    ollama_model = StringField('Ollama Model', validators=[DataRequired(), Length(max=200)])
    submit = SubmitField('Save Settings')

class BackupForm(FlaskForm):
    submit_backup = SubmitField('Backup Settings')
    submit_restore = SubmitField('Restore Settings')

class CharacterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=200)])
    sex = StringField('Sex', validators=[DataRequired(), Length(max=10)])
    age = StringField('Age', validators=[DataRequired(), Length(max=10)])
    traits = TextAreaField('Traits', validators=[DataRequired()])
    behaviors = TextAreaField('Behaviors', validators=[DataRequired()])
    background = TextAreaField('Background', validators=[DataRequired()])
    book_title = StringField('Book Title', validators=[Length(max=200)])
    author = StringField('Author', validators=[Length(max=200)])
    dialogue_examples = TextAreaField('Dialogue Examples')
    genre = StringField('Genre', validators=[Length(max=100)])
    submit = SubmitField('Save Character')

class QuestForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=200)])
    description = TextAreaField('Description', validators=[DataRequired()])
    objectives = TextAreaField('Objectives', validators=[DataRequired()])
    submit = SubmitField('Save Quest')

class UploadForm(FlaskForm):
    file = FileField('Choose PDF file', validators=[DataRequired()])
    submit = SubmitField('Upload')

class GameForm(FlaskForm):
    name = StringField('Game Name', validators=[DataRequired(), Length(min=2, max=100)])
    description = TextAreaField('Description', validators=[DataRequired(), Length(min=10, max=500)])
    submit = SubmitField('Create Game')