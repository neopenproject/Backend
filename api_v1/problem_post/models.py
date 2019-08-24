from settings.database import Base
from sqlalchemy import Column, Integer, String, Boolean


class AnswerPost(Base):
    __tablename__ = 'ANSWER_POST'

    id = Column(Integer, primary_key=True)
    time = Column(Integer)      # 문제를 푼 시간 안씀
    answer_img = Column(String(length=256))
    score = Column(Integer)
    author = Column(String(length=128))
    comment = Column(String(length=512))
    is_over = Column(Boolean)   # 시간 초과 여부
    is_teacher_view = Column(Boolean)  # 강사 확인 여부
    is_grade = Column(Boolean)  # 채점 여부
    is_grade_view = Column(Boolean)    # 채점 확인 여부
    created_at = Column(Integer)
    updated_at = Column(Integer)
