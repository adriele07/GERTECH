from flask import Blueprint, render_template
bp = Blueprint('cursos', __name__)

@bp.route('/cursos')
def abrir_paginadecursos():
    return render_template('cursos.html')