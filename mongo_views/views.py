
#-*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return HttpResponse("<h1 style='color:blue'>欢迎进入mongo监控界面!</h1>"
                        "<h2><a href='/mongos/'>数据库列表</a></h2>")