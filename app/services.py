from app.repositories import UserRepository

class UserService:
    @staticmethod
    def get_all_users():
        return UserRepository.get_all_users()

    @staticmethod
    def create_user(username, password, email):
        return UserRepository.create_user(username, password, email)
    
    @staticmethod
    def authenticate_user(username, password):
        user = UserRepository.get_user_by_username(username)
        if user and user.check_password(password):
            return user
        return None