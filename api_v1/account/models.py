from settings.database import Base
from sqlalchemy import Column, Integer, String


class User(Base):
    __tablename__ = 'USER'

    uid = Column(Integer, primary_key=True)
    name = Column(String(length=256))
    password = Column(String(length=1024))

