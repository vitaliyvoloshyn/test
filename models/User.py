from sqlalchemy import Column, Integer, String

from models.database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    login = Column(String, unique=True)
    password = Column(String)

    def __repr__(self):
        return f'{self.login}'
