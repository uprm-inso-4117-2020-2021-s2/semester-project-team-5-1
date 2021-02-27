from sqlalchemy.dialects.postgresql import UUID
from api import db
import uuid

class User(db.Model):
    REQUIRED_PARAMETERS = {'email', 'password', 'username'}
    
    __tablename__ = 'user'
    user_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    username = db.Column(db.String(30), nullable=False, unique=True)
    email = db.Column(db.String(256), nullable=False, unique=True)
    password = db.Column(db.String(256), nullable=False)
    active = db.Column(db.Boolean, nullable=False, default =False)

    def __init__(self, **args):
        self.username = args.get('username')
        self.email = args.get('email')
        self.password = args.get('password')
        self.active = args.get("active")

    @property
    def pk(self):
        return self.user_id

    @staticmethod
    def getAllUsers():
        return User().query.all()

    @staticmethod
    def getUserById(uid):
        return User().query.filter_by(user_id=uid).first()

    @staticmethod
    def getUserByEmail(uemail):
        return User().query.filter_by(email=uemail).first()

    @staticmethod
    def getUserByUsername(uname):
        return User().query.filter_by(username=uname).first()
    
    def activateUser(self):
        self.active = True
        db.session.commit()
        return self

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self