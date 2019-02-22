from django import forms
from authapp.models import AuthUsers
from mainapp.models import Collections, CollectionsImg
from authapp.forms import UserEditForm

class UserAdminEditForm(UserEditForm):
    class Meta:
        model = AuthUsers
        fields = '__all__'

class ProductEditForm(forms.ModelForm):
    class Meta:
        model = CollectionsImg
        fields = '__all__'

class CollectionsEditForm(forms.ModelForm):
    class Meta:
        model = Collections
        fields = '__all__'