from django.conf.urls import url
from ControlRespberryCard import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^move/$', views.move, name='move'),
]