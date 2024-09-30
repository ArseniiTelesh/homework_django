from django import forms

from catalog.models import Product


class ProductForm(forms.ModelForm):

    prohibited = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

    class Meta:
        model = Product
        fields = '__all__'

    def clean_name(self):

        cleaned_data =  self.cleaned_data['name']

        for word in self.prohibited:
            if word in cleaned_data.lower():
                raise forms.ValidationError('Не поясничай')
        return cleaned_data
