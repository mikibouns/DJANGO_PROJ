from django.core.management.base import BaseCommand
from mainapp.models import Collections, CollectionsImg
# from django.contrib.auth.models import User
from authapp.models import AuthUsers
import json, os

JSON_PATH = r'\mainapp\json'


def loadFromJSON(file_name):
    with open(os.path.join(os.getcwd() + JSON_PATH, file_name + '.json'), 'r') as file:
        return json.load(file)


class Command(BaseCommand):
    def handle(self, *args, **options):
        data_collections = loadFromJSON('collections')
        Collections.objects.all().delete()
        for collection in data_collections:
            new_collections = Collections(**collection)
            new_collections.save()

        data_img = loadFromJSON('collectionsimg')
        CollectionsImg.objects.all().delete()
        for img in data_img:
            collection_name = img["img_collection"]
            # Получаем коллекцию по имени
            _collection_name = Collections.objects.get(collection_name=collection_name)
            # Заменяем название коллекции объектом
            img['img_collection'] = _collection_name
            new_collectionsimg = CollectionsImg(**img)
            new_collectionsimg.save()
        # Создаем суперпользователя при помощи менеджера модели
        super_user = AuthUsers.objects.create_superuser('admin',
                                                        'admin@mail.com', 'admin123', au_age=18)
