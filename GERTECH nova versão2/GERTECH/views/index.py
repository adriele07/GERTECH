from flask import Blueprint, render_template

bp = Blueprint('index', __name__)

@bp.route('/')
def abrir_inicial():
    return render_template('index.html')