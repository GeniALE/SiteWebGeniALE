from django.conf.urls import url

from . import views

app_name = "orchester"
urlpatterns = [
  url(r'^$', views.IndexView.as_view(), name='index'),
  url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
  url(r'^(?P<member_id>\d+)/register/$', views.register, name='register'),
  url(r'^(?P<member_id>\d+)/unregister/$', views.unregister, name='unregister'),
]
