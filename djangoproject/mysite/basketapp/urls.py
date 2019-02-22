from django.conf.urls import url
import basketapp.views as basket_views

urlpatterns = [
    url(r'^$', basket_views.basket, name='edit'),
    url(r'^add/(?P<pk>\d+)/$', basket_views.basket_add, name='add'),
    url(r'^remove/(?P<pk>\d+)/$', basket_views.basket_remove, name='remove'),
    url(r'^quantity_edit/(?P<pk>\d+)/$', basket_views.basket_quantity_edit, name='quantity_edit'),
]
