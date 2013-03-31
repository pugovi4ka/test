from django.forms.models import ModelForm
from django.forms.widgets import TextInput
from mycatalog.models import Product


class CustomColorWidget(TextInput):
    class Media:
        css = {
            'all': ('mycatalog/colorpicker/css/colorpicker.css',)
        }

        js = ('mycatalog/jquery-1.9.1.min.js',
              'mycatalog/colorpicker/js/bootstrap-colorpicker.js',
              'mycatalog/colorpicker-widget.js',
        )

    def __init__(self, *args, **kwargs):
        kwargs['attrs'] = {'class': 'colorpicker'}
        super(CustomColorWidget, self).__init__(*args, **kwargs)


class ProductEditForm(ModelForm):
    class Meta:
        model = Product
        widgets = {'product_color': CustomColorWidget, 'product_color_once_more': CustomColorWidget}

