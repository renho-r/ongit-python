from django.conf.urls import url
from ControlRespberryCar import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^move/$', views.move, name='move'),
]