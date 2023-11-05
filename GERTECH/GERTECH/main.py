from flask import Flask
from views import(
    index
)

def create_app():
    app = Flask(__name__)
    app.secret_key = 'mysecretkey'
    app.register_blueprint(index.bp)
    return app

    
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
    
