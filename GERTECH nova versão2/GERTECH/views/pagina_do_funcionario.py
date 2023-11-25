from flask import Blueprint, render_template

bp = Blueprint('pagina_do_funcionario', __name__)

@bp.route('/cursos_funcionario')
def abrir_pagina_do_funcionario():
    return render_template('cursos.html')

