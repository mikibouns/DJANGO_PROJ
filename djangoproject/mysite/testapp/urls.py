from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<collection_name>\w+)/$', views.ajax_test, name='test1')
]
