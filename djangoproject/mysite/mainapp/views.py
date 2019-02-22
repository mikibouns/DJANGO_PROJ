from django.shortcuts import render
from .models import Collections, CollectionsImg
from basketapp.models import Basket
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


wallpaper_collections = Collections.objects.all().filter(collection_is_active=True).order_by('collection_name')

def basket_func(request):
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(basket_user=request.user)
    return basket

def main(request):
    title = 'index'
    content = {'title': title,
               'basket': basket_func(request),
               'collections': wallpaper_collections,}

    return render(request, 'index.html', content)


def contacts(request):
    title = 'contacts'
    content = {'title': title,
               'basket': basket_func(request),
               'collections': wallpaper_collections}
    return render(request, 'contacts.html', content)


def collections_page(request):
    title = 'collections'
    paginator = Paginator(wallpaper_collections, 3)

    page = request.GET.get('page')
    try:
        page_pagination = paginator.page(page)
    except PageNotAnInteger:
        page_pagination = paginator.page(1)
    except EmptyPage:
        page_pagination = paginator.page(paginator.num_pages)

    content = {'title': title,
               'basket': basket_func(request),
               'collections': wallpaper_collections,
               'page_pagination': page_pagination}
    return render(request, 'collections.html', content)


def product_page(request, collection_name):
    title = 'product_page'
    current_collection = Collections.objects.get(collection_name=collection_name)
    current_wallpaper_img = CollectionsImg.objects.filter(img_collection__collection_name=collection_name, img_is_active=True)
    content = {'title': title,
               'collections': wallpaper_collections,
               'current_collection': current_collection,
               'current_wallpaper_img': current_wallpaper_img,
               'basket': basket_func(request)}
    return render(request, 'product_page.html', content)

