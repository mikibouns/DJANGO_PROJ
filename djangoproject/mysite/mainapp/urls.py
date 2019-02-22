from django.conf.urls import url

import mainapp.views as main_views

urlpatterns = [
    url(r'^(?P<collection_name>\w+)/$', main_views.product_page, name='product_page'),
]
