from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session, relationship

DATABASE_NAME = 'asynchchat.sqlite'
engine = create_engine(f'sqlite:///{DATABASE_NAME}')

session = sessionmaker(bind=engine)
Base = declarative_base()

def create_db():
    Base.metadata.create_all(engine)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    login = Column(String)
    password = Column(String)
    # children = relationship("HistoryUser", "UserContacts")
    def __repr__(self):
        return f'{self.login}'

class HistoryUser(Base):
    __tablename__ = 'history_users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    enter_date = Column(Date)
    ip = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

    def __repr__(self):
        return f'{self.enter_date} {self.ip} {self.user_id}'

class UserContacts(Base):
    __tablename__ = 'users_contacts'
    id = Column(Integer, primary_key=True, autoincrement=True)
    owner_id = Column(Integer, ForeignKey('users.id'))
    user_id = Column(Integer, ForeignKey('users.id'))

    def __repr__(self):
        return f'{self.owner_id} {self.user_id}'




def save_to_db(name: str, password: str):
    user = User(login=name, password=password)
    with Session(engine) as s:
        s.add(user)
        s.commit()

def user_contacts():
    with Session(engine) as s:
        # owner = s.query(User).filter(User.id == 1)
        # print(type(owner))
        # print(owner)
        # user = s.query(User).filter(User.id == 2)
        re = UserContacts(owner_id=2, user_id=3)

        s.add(re)
        s.commit()

def get(ses):
    return ses.query(User).order_by(User.login).offset(3)
def get_users():
    with Session(engine) as s:
        g = get(s)
        return g
def gt():
    with Session(engine) as s:
        return  s.query(UserContacts).filter(UserContacts.owner_id == 1)
