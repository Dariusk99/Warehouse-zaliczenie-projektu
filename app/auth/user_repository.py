from app.auth.user import User

class UserRepository:
    def __init__(self, session):
        self.session = session

    def find_by_username(self, username):
        return self.session.query(User).filter_by(username=username).first()

    def save(self, user):
        self.session.add(user)
        self.session.commit()
        return user
