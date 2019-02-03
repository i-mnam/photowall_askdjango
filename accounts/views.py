from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect(settings.LOGIN_URL) 
            # > http://localhost:8001/accounts/profile/
            # 난 LOGIN_URL:accounts/login 을 호출했는데, LOGIN_REDIRECT_URL인 accounts/profile이 호출되네.
            # login이 호출 될 때, next인자가 없으면 자동으로 리다이렉트 주소가 호출된다고 함.
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {
        'form' : form,
    })


def profile(request):
    return render(request, 'accounts/profile.html') 
    # context_processors 덕에 user데이터를 안남겨도 템플릿에서 바로 호출 및 사용 가능