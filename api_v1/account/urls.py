from api_v1.account.controller import Index
from api_v1.account.customer.views import CustomerAccount, CusAuthView

account_urls = [
    (Index, "/account"),
    (CustomerAccount, "/account/cus"),
    (CusAuthView, '/account/cus/login')
]