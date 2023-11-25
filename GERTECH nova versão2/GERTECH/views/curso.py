from flask import Blueprint, render_template
bp = Blueprint('curso', __name__)

@bp.route('/curso')
def abrir_paginadecursos():
    return render_template('curso.html')