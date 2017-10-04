from django.conf.urls import url
from . import views

app_name = 'op'

urlpatterns = [

    # /music/
    url(r'^list/$', views.IndexView.as_view(), name='index'),

    # /music/712/
    #url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    #url(r'^(?P<pk>[0-9]+)/delete/$', views.ReportDelete.as_view(), name='report-delete'),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.delete, name='report-delete'),

    url(r'^$', views.ReportCreate.as_view(), name='report-add'),

    url(r'^(?P<pk>[0-9]+?)/$', views.updateDetails, name='detail'),
]
