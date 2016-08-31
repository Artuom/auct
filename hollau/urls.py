from django.conf.urls import url, include
from . import views


urlpatterns = [
    # url(r'^$', views.main, name='main'),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^home/$', views.home),
    url(r'^logout/$', views.logout),
    url(r'^ajax/test/$', views.test_ajax, name='ajax'),
]
