from django.conf.urls import url
from . import views

app_name = 'rtv'

urlpatterns = [
    #/rtv/
    url(r'^$',views.index , name ='index'),
    #/rtv/<report_id>/
    url(r'^(?P<report_id>[0-9]+)$',views.detail , name = 'detail'),

]
