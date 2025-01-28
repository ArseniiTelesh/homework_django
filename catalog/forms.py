from django import forms

from catalog.models import Product, Version


class ProductForm(forms.ModelForm):


    class Meta:
        model = Product
        exclude = ['owner']

    prohibited = [
        "казино",
        "криптовалюта",
        "крипта",
        "биржа",
        "дешево",
        "бесплатно",
        "обман",
        "полиция",
        "радар",
    ]

    def clean_name(self):

        cleaned_data = self.cleaned_data["name"]

        if cleaned_data.lower() in self.prohibited:
            raise forms.ValidationError("Не поясничай")

        return cleaned_data

    def clean_description(self):

        cleaned_data = self.cleaned_data["description"]

        if cleaned_data.lower() in self.prohibited:
            raise forms.ValidationError("Не поясничай")

        return cleaned_data


class VersionForm(forms.ModelForm):

    class Meta:
        model = Version
        exclude = "__all__"

    def clean_current_version(self):
        cleaned_data = super().clean()
        current_version = cleaned_data.get('current_version')

        if current_version:
            # Получаем все текущие версии для продукта
            current_versions = Version.objects.filter(product=self.instance.product, current_version=True)

            if self.instance.pk:  # Если это уже существующая версия
                # Исключаем текущую версию из проверки, если она была изменена
                current_versions = current_versions.exclude(pk=self.instance.pk)

            if current_versions.exists():
                raise forms.ValidationError("Может быть только одна активная версия.")

        # Возвращаем значение флажка current_version
        return current_version
