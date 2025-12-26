from werkzeug.security import generate_password_hash, check_password_hash
from app.auth.user import User

class AuthService:
    def __init__(self, user_repo):
        self.user_repo = user_repo

    def register(self, username, password):
        if self.user_repo.find_by_username(username):
            return None

        user = User(
            username=username,
            password_hash=generate_password_hash(password)
        )
        return self.user_repo.save(user)

    def authenticate(self, username, password):
        user = self.user_repo.find_by_username(username)
        if not user:
            return None

        if not check_password_hash(user.password_hash, password):
            return None

        return user
