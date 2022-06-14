from django.shortcuts import render
from .models import ApiStep,ApiTest
from django.http import HttpResponse
from django.http import request
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.
# 接口管理
@login_required
def apitest_manage(request):
    apitest_list = ApiTest.objects.all()
    username = request.session.get('user', '')
    return render(request, 'apitest_manage.html',
                  {'user':username,'apitests':apitest_list})


# 接口步骤管理
@login_required
def apistep_manage(request):
    username = request.session.get('user', '')
    apistep_list = ApiStep.objects.all()
    return render(request, "apistep_manage.html",
                  {'user':username,'apisteps':apistep_list})