from flask import render_template, request, redirect
from app import app
from modules.player import Player
from modules.game import Game

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<choice1>', methods=["POST"])
def get_choices(choice1):
    choice2 = Player.make_choice()
    return redirect(f'/{choice1}/{choice2}')

@app.route('/<choice1>/<choice2>')
def play_a_game(choice1, choice2):
    player1 = Player("John", choice1)
    player2 = Player("Computer", choice2)
    game = Game(player1, player2)
    winner = game.play_game()
    return render_template('results.html', winner=winner)