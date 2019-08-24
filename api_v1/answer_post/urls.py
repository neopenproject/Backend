from api_v1.answer_post.views import AnswerPost, AnswerPostPk

answer_post_urls = [
    (AnswerPostPk, "/answer/post/<int:post_id>"),
    (AnswerPost, "/answer/post")
]