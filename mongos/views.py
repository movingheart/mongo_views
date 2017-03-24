# -*- coding:utf-8 -*-
import datetime
from django.shortcuts import render
from utils.operate_mysql import get_data
from utils.settings import MYSQL_KW
from models import RemarkForm


def mongos(request):
    """获取所有的库名"""
    sql = "select DISTINCT mongo_base from handle_mongo order by mongo_base"

    data = get_data(sql, **MYSQL_KW)
    return render(request, 'mongos/index.html', {"database_list": data})


def detail(request, base):
    """列出此库下所有的集合"""
    sql = "select DISTINCT mongo_col from handle_mongo WHERE mongo_base='%s'" % base
    data = get_data(sql, **MYSQL_KW)
    return render(request, 'mongos/detail.html', {"database": base, "col_list": data})


def charts(request, base, col):
    """列出此集合的100条记录"""
    if request.method == 'POST':
        # 接收时间参数
        start_year = request.POST.get("start_time_year")
        start_month = request.POST.get("start_time_month")
        start_day = request.POST.get("start_time_day")
        end_year = request.POST.get("end_time_year")
        end_month = request.POST.get("end_time_month")
        end_day = request.POST.get("end_time_day")
        start = "-".join([start_year, start_month, start_day])
        end = "-".join([end_year, end_month, end_day])
        sql = ("select `update_count`,`timestamp` from handle_mongo "
               "WHERE mongo_base='%s' and mongo_col='%s' "
               "and timestamp between  '%s' and '%s' "
               "ORDER BY `timestamp` limit 100") % (base, col, start, end)
    else:
        sql = ("select `update_count`,`timestamp` from handle_mongo "
              "WHERE mongo_base='%s' and mongo_col='%s' "
               "ORDER BY `timestamp` limit 100") % (base, col)

    data = get_data(sql, **MYSQL_KW)
    title = "%s.%s charts" % (base, col)
    categories = []
    datas = []
    for record in data:
        categories.append(record['timestamp'].strftime("%Y-%m-%d %H:%M"))
        datas.append(int(record['update_count']))
    form = RemarkForm()
    return render(request, 'mongos/charts.html', {"database": base,
                                                  "collection": col,
                                                  "title": title,
                                                  "categories": categories,
                                                  "data": datas,
                                                  "form": form})
