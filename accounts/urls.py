from django.conf.urls import url
from django.contrib.auth.views import login, logout
from . import views


# django.contrib.auth 
# http://localhost:8001/accounts/login/?next=/blog/1/comment/new/
# TemplateDoesNotExist at /accounts/login/
# registration/login.html > with kwargs's template_name's value > account/login_form.html

# 로그인할 때 사용되는 뷰가 django.contrib.auth.views.login이여서 이곳 accounts/views는 사용되지 않았다. 
# 좌측 뷰에서는 login할 때 next인자가 기본으로 들어오는 걸로 기억한다.

# 기본적인 logout은 관리자페이지에서 이루어짐. http://localhost:8001/accounts/logout/ 주소는 이건데 관리자모드에서 이뤄짐.
urlpatterns = [
    url(r'^login/$', login, name='login', kwargs={
        'template_name':'accounts/login_form.html',
    }),
    url(r'^logout/$', logout, name='logout', kwargs={
        'next_page' : 'login', # url name으로 적었네?!
    }),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^profile/$', views.profile, name='profile'),
]