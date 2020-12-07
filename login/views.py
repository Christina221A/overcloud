# login/views.py
from django.shortcuts import render, redirect
from login.models import Users
from .forms import UserForm


def index(request):
    pass
    return render(request, 'login/index.html')


def login(request):
    if request.session.get('is_login', None):
        return redirect('/login/#')
    if request.method == "POST":
        login_form = UserForm(request.POST)
        message = "Please fill in all blanks."
        if login_form.is_valid():  # 确保用户名和密码都不为空
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            # 用户名字符合法性验证
            # 密码长度验证
            # 更多的其它验证.....
            try:
                user = Users.objects.get(name=username)
                if user.password == password:
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.name
                    return redirect('/login/#')
                else:
                    message = "Incorrect password."
            except:
                message = "Invalid username."
        return render(request, 'login/login.html', locals())
    login_form = UserForm()
    return render(request, 'login/login.html', locals())


def register(request):
    pass
    return render(request, 'login/register.html')


def logout(request):
    # if request.session.get('is_login', None):
    #     return redirect('/login/#')
    request.session.flush()
    return redirect('/login/login')
