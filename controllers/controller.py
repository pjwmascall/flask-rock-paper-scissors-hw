from flask import render_template, request, redirect
from app import app
from modules.player import Player
from modules.game import Game

@app.route('/')
def index():
    return render_template('index.html')