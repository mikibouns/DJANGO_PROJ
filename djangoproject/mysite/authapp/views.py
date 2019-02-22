from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse

from .forms import UserLoginForm
from mainapp.models import Collections
from mainapp.views import basket_func
from .forms import UserRegisterForm
from .forms import UserEditForm


wallpaper_collections = Collections.objects.all().order_by('collection_name')

def login(request):
    title = 'login'

    login_form = UserLoginForm(data=request.POST)
    if request.method == 'POST' and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('main'))

    content = {'title': title,
               'login_form': login_form,
               'collections': wallpaper_collections}
    return render(request, 'authapp/login.html', content)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main'))

def register(request):
    title = 'register'

    if request.method == 'POST':
        register_form = UserRegisterForm(request.POST, request.FILES)
        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        register_form = UserRegisterForm()
    content = {'title': title,
               'register_form': register_form,
               'collections': wallpaper_collections}
    return render(request, 'authapp/register.html', content)

def edit(request):
    title = 'edit_user'
    if request.method == 'POST':
        edit_form = UserEditForm(request.POST, request.FILES,
                                     instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        edit_form = UserEditForm(instance=request.user)
    content = {'title': title,
               'edit_form': edit_form,
               'collections': wallpaper_collections,
               'basket': basket_func(request)}
    return render(request, 'authapp/edit.html', content)