from django.forms.models import ModelForm
from mycatalog.models import Product


class ProductEditForm(ModelForm):
    class Meta:
        model = Product


