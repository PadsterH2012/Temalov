from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from app.forms import GameForm
from shared.models.entities import Game, PlayerGame
from app import db
main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/welcome')
@login_required
def welcome():
    return render_template('welcome.html')

@main_bp.route('/games', methods=['GET', 'POST'])
@login_required
def games():
    form = GameForm()
    if form.validate_on_submit():
        game = Game(name=form.name.data, description=form.description.data)
        db.session.add(game)
        db.session.commit()
        flash('Game has been created!', 'success')
        return redirect(url_for('main.games'))
    games = Game.query.all()
    return render_template('games.html', form=form, games=games)

@main_bp.route('/join_game/<int:game_id>')
@login_required
def join_game(game_id):
    game = Game.query.get_or_404(game_id)
    if not PlayerGame.query.filter_by(player_id=current_user.id, game_id=game.id).first():
        player_game = PlayerGame(player_id=current_user.id, game_id=game.id)
        db.session.add(player_game)
        db.session.commit()
        flash('You have joined the game!', 'success')
    return redirect(url_for('main.games'))
