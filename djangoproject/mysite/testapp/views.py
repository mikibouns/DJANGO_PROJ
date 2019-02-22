from django.shortcuts import render
from mainapp.models import Collections, CollectionsImg
from mainapp.views import wallpaper_collections



def ajax_test(request, collection_name):
    title = 'test'
    current_wallpaper_img = CollectionsImg.objects.filter(img_collection__collection_name=collection_name)
    current_collection = Collections.objects.get(collection_name=collection_name)
    context = {'title': title,
               'current_collection': current_collection,
               'current_wallpaper_img': current_wallpaper_img,
               'collections': wallpaper_collections}
    return render(request, 'testapp/test1.html', context)
