from flask import Blueprint, render_template
bp = Blueprint('pagina_do_administrador', __name__)

@bp.route('/')
def abrir_pagina_do_administrador():
    return render_template('pagina_do_administrador.html')