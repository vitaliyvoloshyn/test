from sqlalchemy import Column, Integer, String, Date, ForeignKey

from models.create_database import Base


class UserHistory(Base):
    __tablename__ = 'history_users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    enter_date = Column(Date)
    ip = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

    def __repr__(self):
        return f'{self.enter_date} {self.ip} {self.user_id}'
