from settings.database import Base
from sqlalchemy import Column, Integer, String, VARCHAR


class Customer(Base):
    __tablename__ = 'CUSTOMER'

    cid = Column(String(length=128), primary_key=True)  # CID{TIMESTAMP}
    email = Column(String(length=512), nullable=False, unique=True)
    password = Column(String(length=1024), nullable=False)
    salt = Column(String(length=256), nullable=False)


class Teacher(Base):
    __tablename__ = 'TEACHER'

    tid = Column(String(length=128), primary_key=True)
    email = Column(String(length=512), nullable=False, unique=True)
    password = Column(String(length=1024), nullable=False)
    affiliation = Column(String(length=256))
    salt = Column(String(length=256), nullable=False)
    created_at = Column(Integer)
    updated_at = Column(Integer)
