from django import forms
from .models import Product, Brand
from django.forms import ModelForm


class BrandCreateForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ["brand_name"]
    # brand= forms.CharField()


class ProductCreateForm(ModelForm):

    class Meta:
        model = Product
        fields = "__all__"
        widgets = {
            "mobile_name": forms.TextInput(attrs={'class': 'form-control'}),
            "price": forms.TextInput(attrs={'class': 'form-control'}),
            "specs": forms.TextInput(attrs={'class': 'form-control'})
        }

        def clean(self):
            cleaned_data = super().clean()
            price = cleaned_data.get('price')
            if int(price) < 500:
                msg = "invalid price"
                self.add_error("price", msg)
