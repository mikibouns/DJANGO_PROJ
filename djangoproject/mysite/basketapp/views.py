from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from .models import Basket
from mainapp.models import Collections, CollectionsImg
from mainapp.views import basket_func, wallpaper_collections
from django.contrib.auth.decorators import login_required

@login_required
def basket(request):
    title = 'basket'
    content = {'basket': basket_func(request),
               'title': title,
               'collections': wallpaper_collections}
    return render(request, 'basketapp/basket.html', content)

@login_required
def basket_add(request, pk):
    product = get_object_or_404(CollectionsImg, pk=pk)
    old_basket_item = Basket.objects.filter(basket_user=request.user, basket_product=product)
    if product.img_is_active:# проверяет активен ли товар
        quantity = 1
        if request.method == 'POST':
            quantity = request.POST.get('quantity')
        if old_basket_item:
            old_basket_item[0].basket_quantity += int(quantity)
            old_basket_item[0].save()
        else:
            new_basket_item = Basket(basket_user=request.user, basket_product=product)
            new_basket_item.basket_quantity += int(quantity)
            new_basket_item.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def basket_remove(request, pk):
    basket_record = get_object_or_404(Basket, pk=pk)
    basket_record.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def basket_quantity_edit(request, pk):
    basket_record = get_object_or_404(Basket, pk=pk)
    if request.method == 'POST':
        quantity = request.POST.get('quantity')
        basket_record.basket_quantity = quantity
        basket_record.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))