from api_v1.account.controller import Index
from api_v1.account.customer.views import CustomerAccount, CusAuthView
from api_v1.account.teacher.views import TeacherAccount, TeaAuthView

account_urls = [
    (Index, "/account"),
    (CustomerAccount, "/account/cus"),
    (CusAuthView, '/account/cus/login'),

    (TeacherAccount, "/account/teacher"),
    (TeaAuthView, '/account/teacher/login')
]