from django.conf.urls import url
from . import views

app_name = 'rtv'

urlpatterns = [
    #/rtv/
    url(r'^$',views.IndexView.as_view() , name ='index'),
    #/rtv/<report_id>/
    url(r'^(?P<pk>[0-9]+)$',views.DetailView.as_view() , name = 'detail'),

]
