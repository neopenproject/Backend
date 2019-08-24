from api_v1.account.urls import account_urls
from api_v1.api_index_views import ApiV1Index
from api_v1.problem_post.urls import problem_post_urls
from api_v1.answer_post.urls import answer_post_urls
from api_v1.media.urls import media_urls

prefix_url = '/api/v1'

urlpatterns = [
                  (ApiV1Index, '')
] + account_urls + \
              answer_post_urls + \
              problem_post_urls + \
              media_urls

