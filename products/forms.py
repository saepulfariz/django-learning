from django import forms
from .models import Product

class ProductForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'placeholder': 'Enter product name'})
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'placeholder': 'Enter product description'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})
        self.fields['price'].widget.attrs.update({'placeholder': 'Enter product price'})
        self.fields['price'].widget.attrs.update({'class': 'form-control'})
        self.fields['image'].widget.attrs.update({'placeholder': 'Upload product image'})
        self.fields['image'].widget.attrs.update({'class': 'form-control-file'})

    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image']
        labels = {
            'name': 'Product Name',
            'description': 'Description',
            'price': 'Price',
            'image': 'Product Image'
        }