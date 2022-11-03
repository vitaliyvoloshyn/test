from sqlalchemy import Column, Integer, ForeignKey

from models.create_database import Base


class UserContacts(Base):
    __tablename__ = 'users_contacts'
    id = Column(Integer, primary_key=True, autoincrement=True)
    owner_id = Column(Integer, ForeignKey('users.id'))
    user_id = Column(Integer, ForeignKey('users.id'))

    def __repr__(self):
        return f'{self.owner_id} {self.user_id}'
