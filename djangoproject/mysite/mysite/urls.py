"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

import mainapp.views as main_views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^admin/', include('adminapp.urls', namespace='admin')),
    url(r'^$', main_views.main, name='main'),
    url(r'^contacts/$', main_views.contacts, name='contacts'),
    url(r'^collections/$', main_views.collections_page, name='collections'),
    url(r'^collections/', include('mainapp.urls', namespace='products')),
    url(r'^auth/', include('authapp.urls', namespace='auth')),
    url(r'^basket/', include('basketapp.urls', namespace='basket')),

    url(r'^test/', include('testapp.urls', namespace='test'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
