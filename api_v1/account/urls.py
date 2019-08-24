from api_v1.account.customer.views import CustomerAccount, CusAuthView
from api_v1.account.teacher.views import TeacherAccount, TeaAuthView

account_urls = [
    (CustomerAccount, "/account/cus"),
    (CusAuthView, '/account/cus/login'),

    (TeacherAccount, "/account/teacher"),
    (TeaAuthView, '/account/teacher/login')
]