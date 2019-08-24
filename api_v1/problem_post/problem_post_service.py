from settings.database import session_scope
from api_v1.problem_post.models import ProblemPost
from Utils.utils import set_response, upload_img
from datetime import datetime as dt


class ProblemPostService:
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


