from flask import Flask
from views import(
    index,
    cursos,
    cadastro1,
    pagina_do_administrador

)

def create_app():
    app = Flask(__name__)
    app.secret_key = 'mysecretkey'
    app.register_blueprint(index.bp)
    app.register_blueprint(cursos.bp)
    app.register_blueprint(cadastro1.bp)
    app.register_blueprint(pagina_do_administrador.bp)
    

    return app

    
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
    
