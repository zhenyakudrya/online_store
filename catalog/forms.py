from django import forms

from catalog.models import Product, Version


class StyleFormMixin:
    def init(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ('product_name', 'product_content', 'product_image', 'category', 'price_for_one')

    def clean_product_name(self):
        cleaned_data = self.cleaned_data['product_name']
        wrong_product_name = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                              'радар']
        for word in wrong_product_name:
            if word in cleaned_data:
                raise forms.ValidationError('Недопустимое название продукта')
        return cleaned_data

    def clean_product_content(self):
        cleaned_data = self.cleaned_data['product_content']
        wrong_content_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                               'радар']
        for word in wrong_content_words:
            if word in cleaned_data:
                raise forms.ValidationError('Недопустимое название в описании')
        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'
