# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth import authenticate, login
from apitest.models import Apitest, Apistep, Apis


def test(request):
    return HttpResponse('''本站介绍linux如何查看端口被哪个进程占用的方法：
1、lsof -i:端口号
2、netstat -tunlp|grep 端口号
都可以查看指定端口被哪个进程占用的情况.''')



def login(request):
    if request.POST:
        username = password = ''
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            request.session['user'] = username
            response = HttpResponseRedirect('/home/')
            return response
        else:
            return render(request, 'login1.html', {'error': 'username or password error'})
    return render(request, 'login.html')


def home(request):
    return render(request, "home.html")


def logout(request):
    auth.logout(request)
    return render(request, 'login.html')


# 接口管理
@login_required
def apitest_manage(request):
    apitest_list = Apitest.objects.all()
    username = request.session.get('user', '')
    return render(request, "apitest_manage.html", {"user": username, "apitests": apitest_list})


# 接口步骤管理
@login_required
def apistep_manage(request):
    apistep_list = Apistep.objects.all()
    username = request.session.get('user', '')
    return render(request, "apistep_manage.html", {'user': username, 'apisteps': apistep_list})


@login_required
def apis_manage(request):
    username = request.session.get('user', '')
    apis_list = Apis.objects.all()
    return render(request, "apis_manage.html", {"user": username, "apiss": apis_list})
