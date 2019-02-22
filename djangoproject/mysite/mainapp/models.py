from django.db import models

class Collections(models.Model):
    collection_name = models.CharField(verbose_name='collection', max_length=32, blank=True, unique=True)
    collection_description = models.TextField(verbose_name='description', blank=True, null=True)
    collection_price = models.DecimalField(verbose_name='price', max_digits=10, decimal_places=2)
    collection_title_img = models.ImageField(verbose_name='title_img', blank=True, upload_to='media')
    collection_is_active = models.BooleanField(verbose_name='active', default=True)

    def __str__(self):
        return self.collection_name


class CollectionsImg(models.Model):
    img_name = models.CharField(verbose_name='name', max_length=32, blank=True, unique=True)
    img_img = models.ImageField(verbose_name='img', blank=True, upload_to='media')
    img_collection = models.ForeignKey(Collections, on_delete=models.CASCADE)
    img_is_active = models.BooleanField(verbose_name='active', default=True)

    def __str__(self):
        return self.img_name