from faker import Faker
from faker.providers import internet
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from models.User import User
from models.database import create_db, engine
from models.hash import hash_password


def create_database(load_fake_data: bool = True):
    create_db()
    if load_fake_data:
        __insert_fake_data()


def __insert_fake_data():
    fake = Faker('ru_RU')
    fake.add_provider(internet)
    users = []
    with Session(engine) as session:
        for _ in range(10):
            login = fake.user_name()
            password = fake.password(4)
            print(f'login - {login}, pass - {password}')
            password = hash_password(password)
            users.append(User(login=login, password=password))
        session.add_all(users)
        session.commit()

def add_user(login, pswd):
    with Session(engine) as session:
        password = hash_password(pswd)
        user = User(login=login, password=password)
        session.add(user)
        try:
            session.commit()
        except IntegrityError as er:
            print("ошибочка")
        except Exception as e:
            print(e.__class__)
