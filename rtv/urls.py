from django.conf.urls import url
from . import views

app_name = 'rtv'

urlpatterns = [
    #/rtv/
    url(r'^$',views.IndexView.as_view() , name ='index'),
    #/rtv/<pk>/
    url(r'^(?P<pk>[0-9]+)$',views.DetailView.as_view() , name = 'detail'),
    #/rtv/report/add/
    url(r'^report/add$',views.ReportCreate.as_view() , name = 'report-add'),
    #/rtv/report/1/
    url(r'^report/(?P<pk>[0-9]+)/$',views.ReportUpdate.as_view() , name = 'report-update'),

    #/rtv/report/1/delete
    url(r'^report/(?P<pk>[0-9]+)/delete/$',views.ReportDelete.as_view() , name = 'report-delete'),

]
