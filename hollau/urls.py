from django.conf.urls import url, include
from . import views


urlpatterns = [
    # url(r'^$', views.main, name='main'),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^home/$', views.home),
    url(r'^logout/$', views.logout),
    url(r'^add_lot/$', views.add_lot, name='add_lot'),
    url(r'^lot_edit/(?P<pk>[0-9]+)/$', views.lot_edit, name='lot_edit'),
    url(r'^lot_detail/(?P<pk>[0-9]+)/$', views.lot_detail, name='lot_detail'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.category, name='category'),
    url(r'^section_check/$', views.section_check, name='section_check'),
    url(r'^add_category/$', views.add_category, name='add_category'),
    url(r'^make_bet/$', views.make_bet, name='make_bet'),
    url(r'^test_form/$', views.test_form, name='test_form'),
    url(r'^test_ajax/$', views.test_ajax, name='tets_ajax'),
    url(r'^countdown/$', views.countdown, name='countdown'),
    url(r'^test_check/$', views.test_check, name='test_check'),
    url(r'^check_update/$', views.check_update, name='check_update'),
]