from django.conf.urls import url
import adminapp.views as admin_views

urlpatterns = [
    url(r'^users/create/$', admin_views.user_create, name='user_create'),
    url(r'^users/read/$', admin_views.users, name='users'),
    url(r'^users/update/(?P<pk>\d+)/$', admin_views.user_update, name='user_update'),
    url(r'^users/delete/(?P<pk>\d+)/$', admin_views.user_delete, name='user_delete'),

    url(r'^products/read/(?P<list_filter>\w+)/$', admin_views.products, name='products'),
    url(r'^products/create/$', admin_views.products_create, name='products_create'),
    url(r'^products/update/(?P<pk>\d+)/$', admin_views.products_update, name='products_update'),
    url(r'^products/delete/(?P<pk>\d+)/$', admin_views.products_delete, name='products_delete'),

    url(r'^collections/read/$', admin_views.collections, name='collections'),
    url(r'^collections/create/$', admin_views.collections_create, name='collections_create'),
    url(r'^collections/update/(?P<pk>\d+)/$', admin_views.collections_update, name='collections_update'),
    url(r'^collections/delete/(?P<pk>\d+)/$', admin_views.collections_delete, name='collections_delete'),
]
