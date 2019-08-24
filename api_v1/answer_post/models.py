from settings.database import Base
from sqlalchemy import Column, Integer, String


class ProblemPost(Base):
    __tablename__ = 'PROBLEM_POST'

    id = Column(Integer, primary_key=True)
    max_time = Column(Integer)
    title = Column(String(length=256))
    subject = Column(String(length=32))
    category = Column(String(length=32))
    problem_img = Column(String(length=256))
    view = Column(Integer)
    author = Column(String(length=128))
    affiliation = Column(Integer)
    created_at = Column(Integer)
    updated_at = Column(Integer)