class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:123@localhost:5432/flaskappdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'your_secret_key'  
    JWT_SECRET_KEY = 'your_jwt_secret_key'