from django.conf.urls import url
import authapp.views as auth_views

urlpatterns = [
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^register/$', auth_views.register, name='register'),
    url(r'^edit/$', auth_views.edit, name='edit'),
]
