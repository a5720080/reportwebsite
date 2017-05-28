from django.conf.urls import url
from . import views

urlpatterns = [
    #/rtv/
    url(r'^$',views.index , name ='index'),
    #/rtv/123/
    url(r'^(?P<report_id>[0-9]+)$',views.detail , name = 'detail'),
]
