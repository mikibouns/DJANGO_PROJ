from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test
# from django.views.generic.list import ListView
# from django.utils.decorators import method_decorator

from authapp.models import AuthUsers
from mainapp.models import Collections, CollectionsImg
from mainapp.views import wallpaper_collections
from authapp.forms import UserRegisterForm
from adminapp.forms import ProductEditForm, CollectionsEditForm, UserAdminEditForm
from mainapp.views import basket_func


###################################### USERS ###############################################

@user_passes_test(lambda u: u.is_superuser)
def users(request):
    title = 'users'
    users_list = AuthUsers.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username')
    content = {'title': title,
               'basket': basket_func(request),
               'objects': users_list,
               'collections': wallpaper_collections, }
    return render(request, 'adminapp/users.html', content)


@user_passes_test(lambda u: u.is_superuser)
def user_create(request):
    title = 'create_user'
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST, request.FILES)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('admin:users'))
    else:
        user_form = UserRegisterForm()
    content = {'title': title,
               'basket': basket_func(request),
               'collections': wallpaper_collections,
               'update_form': user_form}
    return render(request, 'adminapp/user_update.html', content)


@user_passes_test(lambda u: u.is_superuser)
def user_update(request, pk):
    title = 'user_update'
    edit_user = get_object_or_404(AuthUsers, pk=pk)
    if request.method == 'POST':
        edit_form = UserAdminEditForm(request.POST, request.FILES, instance=edit_user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('admin:user_update', args=[edit_user.pk]))
    else:
        edit_form = UserAdminEditForm(instance=edit_user)
    content = {'title': title,
               'basket': basket_func(request),
               'update_form': edit_form,
               'collections': wallpaper_collections, }
    return render(request, 'adminapp/user_update.html', content)


@user_passes_test(lambda u: u.is_superuser)
def user_delete(request, pk):
    title = 'user_delete'
    user = get_object_or_404(AuthUsers, pk=pk)
    if request.method == 'POST':
        # user.delete()
        user.is_active = False
        user.save()
    content = {'title': title,
               'basket': basket_func(request),
               'user_to_delete': user}
    return render(request, 'adminapp/user_delete.html', content)


###################################### PRODUCTS ###############################################

@user_passes_test(lambda u: u.is_superuser)
def products(request, list_filter):
    title = 'products_list'
    if list_filter == 'all':
        products_list = CollectionsImg.objects.all().order_by('img_collection')
    else:
        products_list = CollectionsImg.objects.filter(img_collection__collection_name=list_filter).order_by(
            'img_collection')
    context = {'title': title,
               'object_list': products_list,
               'basket': basket_func(request),
               'collections': wallpaper_collections}
    return render(request, 'adminapp/products_list.html', context)


@user_passes_test(lambda u: u.is_superuser)
def products_create(request):
    title = 'products_crete'
    if request.method == 'POST':
        product_form = ProductEditForm(request.POST, request.FILES)
        if product_form.is_valid():
            product_form.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        product_form = ProductEditForm()
    context = {'title': title,
               'update_form': product_form,
               'basket': basket_func(request),
               'collections': wallpaper_collections}
    return render(request, 'adminapp/products_update.html', context)


@user_passes_test(lambda u: u.is_superuser)
def products_update(request, pk):
    title = 'products_update'
    edit_product = get_object_or_404(CollectionsImg, pk=pk)
    if request.method == 'POST':
        edit_form = ProductEditForm(request.POST, request.FILES, instance=edit_product)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('admin:products_update', args=[edit_product.pk]))
    else:
        edit_form = ProductEditForm(instance=edit_product)
    content = {'title': title,
               'update_form': edit_form,
               'basket': basket_func(request),
               'collections': wallpaper_collections, }
    return render(request, 'adminapp/products_update.html', content)


@user_passes_test(lambda u: u.is_superuser)
def products_delete(request, pk):
    title = 'products_delete'
    product = get_object_or_404(CollectionsImg, pk=pk)
    if request.method == 'POST':
        # product.delete()
        product.img_is_active = False
        product.save()
    context = {'title': title,
               'product_to_delete': product,
               'basket': basket_func(request),
               'collections': wallpaper_collections}
    return render(request, 'adminapp/products_delete.html', context)


###################################### COLLECTIONS ###############################################

# class CollectionsListView(ListView):
#     model = Collections
#     # paginate_by = 2
#     template_name = 'adminapp/collections_list.html'
#
#     @method_decorator(user_passes_test(lambda u: u.is_superuser))
#     def dispatch(self, *args, **kwargs):
#         return super(CollectionsListView, self).dispatch(*args, **kwargs)

#     @method_decorator(user_passes_test(lambda u: u.is_superuser))
#     def get_context (self, *args, **kwargs):
#         return super(CollectionsListView, self).dispatch(*args, **kwargs)

@user_passes_test(lambda u: u.is_superuser)
def collections(request):
    title = 'collections_list'
    collections_list = Collections.objects.all().order_by('collection_name')
    context = {'title': title,
               'object_list': collections_list,
               'basket': basket_func(request),
               'collections': wallpaper_collections}
    return render(request, 'adminapp/collections_list.html', context)


@user_passes_test(lambda u: u.is_superuser)
def collections_create(request):
    title = 'collections_crete'
    if request.method == 'POST':
        collection_form = CollectionsEditForm(request.POST, request.FILES)
        if collection_form.is_valid():
            collection_form['']
            collection_form.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        collection_form = CollectionsEditForm()
    context = {'title': title,
               'update_form': collection_form,
               'basket': basket_func(request),
               'collections': wallpaper_collections}
    return render(request, 'adminapp/products_update.html', context)


@user_passes_test(lambda u: u.is_superuser)
def collections_update(request, pk):
    title = 'collections_update'
    edit_collections = get_object_or_404(Collections, pk=pk)
    if request.method == 'POST':
        edit_form = CollectionsEditForm(request.POST, request.FILES, instance=edit_collections)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('admin:collections_update', args=[edit_collections.pk]))
    else:
        edit_form = CollectionsEditForm(instance=edit_collections)
    content = {'title': title,
               'update_form': edit_form,
               'basket': basket_func(request),
               'collections': wallpaper_collections, }
    return render(request, 'adminapp/products_update.html', content)


@user_passes_test(lambda u: u.is_superuser)
def collections_delete(request, pk):
    title = 'collections_delete'
    collection = get_object_or_404(Collections, pk=pk)
    if request.method == 'POST':
        # collection.delete()
        collection.collection_is_active = False
        collection.save()
    context = {'title': title,
               'collection_to_delete': collection,
               'basket': basket_func(request),
               'collections': wallpaper_collections}
    return render(request, 'adminapp/collections_delete.html', context)
