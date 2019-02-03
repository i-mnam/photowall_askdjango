from django.conf.urls import url
from django.contrib.auth.views import login
from . import views


# django.contrib.auth 
# http://localhost:8001/accounts/login/?next=/blog/1/comment/new/
# TemplateDoesNotExist at /accounts/login/
# registration/login.html > with kwargs's template_name's value > account/login_form.html

# 로그인할 때 사용되는 뷰가 django.contrib.auth.views.login이여서 이곳 accounts/views는 사용되지 않았다. 
# 좌측 뷰에서는 login할 때 next인자가 기본으로 들어오는 걸로 기억한다.
urlpatterns = [
    url(r'^login/$', login, name='login', kwargs={
        'template_name':'accounts/login_form.html',
    }),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^profile/$', views.profile, name='profile'),
]