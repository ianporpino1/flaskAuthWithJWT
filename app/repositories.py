from app.models import User
from app import db

class UserRepository:
    @staticmethod
    def get_all_users():
        return User.query.all()

    @staticmethod
    def create_user(username, password, email):
        new_user = User(username=username, email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        return new_user
    
    @staticmethod
    def get_user_by_username(username):
        return User.query.filter_by(username=username).first()