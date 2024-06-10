

from flask import Flask
from app.models import db
from app.routes import register_routes
from flask_jwt_extended import JWTManager

def create_app():
    app = Flask(__name__)
    
    # Configurações do banco de dados
    app.config.from_object('config.Config')
    
    db.init_app(app)

    jwt = JWTManager(app)
    
    # Registrar rotas
    register_routes(app)
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)