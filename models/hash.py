import hashlib
import os

from models.User import User
from models.database import Session, engine


def hash_password(pswd, salt = None):
    if not salt:
        salt = os.urandom(32)  # Новая соль для данного пользователя
    key = hashlib.pbkdf2_hmac('sha256', pswd.encode('utf-8'), salt, 100000)
    return salt+key

def check_password(login, pswd = None):
    with Session() as session:
        res = session.query(User).filter(User.login == login).first()
        if res.password == hash_password(pswd=pswd, salt=res.password[:32]):
            return True
        else:
            return False
