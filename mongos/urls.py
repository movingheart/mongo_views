from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.mongos, name='mongos'),
    url(r'^(?P<base>\w+)/$', views.detail, name='detail'),
    url(r'^(?P<base>\w+)/(?P<col>\S+)$', views.charts, name='charts'),
]
