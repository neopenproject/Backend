from settings.database import session_scope
from api_v1.problem_post.models import ProblemPost
from api_v1.answer_post.models import AnswerPost
from Utils.utils import set_response, upload_img
from datetime import datetime as dt


class ProblemPostService:
    @classmethod
    def mysql_fetch_problem_post(cls, filters=None):
        problem_post_list = []
        with session_scope() as session:
            filter_list = []
            for filter in filters.items():
                key = filter[0]
                value = filter[1]
                if key == 'affiliation':
                    filter_list.append(ProblemPost.affiliation == value)

            if filters.get('order') is not None:
                problem_model = session.query(ProblemPost).filter(*filter_list).order_by(ProblemPost.view.desc())
            else:
                problem_model = session.query(ProblemPost).filter(*filter_list).order_by(ProblemPost.updated_at.desc())

            for problem in problem_model:
                count = session.query(AnswerPost).filter(AnswerPost.problem_post == problem.id).distinct(
                    AnswerPost.author).count()
                obj = {
                    'id': problem.id,
                    'max_time': problem.max_time,
                    'title': problem.title,
                    'sub_title': problem.sub_title,
                    'subject': problem.subject,
                    'category': problem.category,
                    'problem_img': problem.problem_img,
                    'view': problem.view,
                    'author': problem.author,
                    'affiliation': problem.affiliation,
                    'created_at': problem.created_at,
                    'updated_at': problem.updated_at,
                    'count': count
                }
                problem_post_list.append(obj)
        return problem_post_list

    @classmethod
    def mysql_create_problem_post(cls, params, file=None):
        problem_post = {}
        if file is not None:
            img_path = upload_img('problems', file)
            params['problem_img'] = img_path

        with session_scope() as session:
            now = int(dt.now().timestamp() * 10000000)
            params['view'] = 0
            params['created_at'] = now
            params['updated_at'] = now
            problem_post_model = ProblemPost(**params)
            session.add(problem_post_model)
            response = set_response("00", {"successMsg": "성공적으로 등록되었습니다."})

        return response
