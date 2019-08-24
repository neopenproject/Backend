from settings.database import Base
from sqlalchemy import Column, Integer, String, Boolean, BigInteger


class AnswerPost(Base):
    __tablename__ = 'ANSWER_POST'

    id = Column(Integer, primary_key=True)
    time = Column(Integer)  # 문제를 푼 시간 안씀
    answer_img = Column(String(length=256))
    is_over = Column(Boolean)  # 시간 초과 여부
    author = Column(String(length=128))
    is_grade_view = Column(Boolean)  # 채점 확인 여부
    score = Column(Integer)  # 강사 점수
    problem_post = Column(Integer)  # 문제관계
    comment = Column(String(length=512))  # 강사 커맨트
    is_teacher_view = Column(Boolean)  # 강사 확인 여부
    is_grade = Column(Boolean)  # 채점 여부
    created_at = Column(BigInteger)
    updated_at = Column(BigInteger)
