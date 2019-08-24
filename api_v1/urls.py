from api_v1.account.urls import account_urls
from api_v1.api_index_views import ApiV1Index

prefix_url = '/api/v1'

urlpatterns = [
                  (ApiV1Index, '')
] + account_urls

