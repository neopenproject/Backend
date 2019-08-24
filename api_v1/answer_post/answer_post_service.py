from settings.database import session_scope
from api_v1.answer_post.models import AnswerPost
from Utils.utils import set_response, upload_img
from datetime import datetime as dt


class AnswerPostService:
    @classmethod
    def mysql_fetch_answer_post(cls, filters=None):
        answer_post_list = []
        with session_scope() as session:
            filter_list = []
            for filter in filters.items():
                key = filter[0]
                value = filter[1]
                if key == 'problem_post':
                    filter_list.append(AnswerPost.problem_post == value)
            answer_model = session.query(AnswerPost).filter(*filter_list)

        count = answer_model.count()

        for answer in answer_model:
            obj = {
                'id': answer.id,
                'time': answer.time,
                'answer_img': answer.answer_img,
                'is_over': answer.is_over,
                'author': answer.author,
                'is_grade_view': answer.is_grade_view,
                'score': answer.score,
                'problem_post': answer.problem_post,
                'comment': answer.comment,
                'is_teacher_view': answer.is_teacher_view,
                'is_grade': answer.is_grade,
                'created_at': answer.created_at,
                'updated_at': answer.updated_at
            }
            answer_post_list.append(obj)

        return count, answer_post_list

    @classmethod
    def mysql_create_answer_post(cls, params, file=None):
        answer_post = {}
        if file is not None:
            img_path = upload_img('answers', file)
            params['answer_img'] = img_path

        with session_scope() as session:
            now = int(dt.now().timestamp() * 10000000)

            params['created_at'] = now
            params['updated_at'] = now
            answer_post_model = AnswerPost(**params)
            session.add(answer_post_model)
            response = set_response("00", {"successMsg": "성공적으로 등록되었습니다."})

        return response
