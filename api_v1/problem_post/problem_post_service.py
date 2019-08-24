from settings.database import session_scope
from api_v1.problem_post.models import ProblemPost
from Utils.utils import set_response, upload_img
from datetime import datetime as dt


class ProblemPostService:
    @classmethod
    def mysql_fetch_problem_post(cls, filter=None):
        problem_post_list = []
        with session_scope() as session:
            problem_model = session.query(ProblemPost).order_by(ProblemPost.updated_at.desc())

            for problem in problem_model:
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
                    'updated_at': problem.updated_at
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
