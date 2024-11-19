from django import forms

from catalog.models import Product, Version


class ProductForm(forms.ModelForm):


    class Meta:
        model = Product
        fields = "__all__"

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

    def clean(self):
        cleaned_data = super().clean()
        current_version = cleaned_data.get('current_version')
        if current_version:
            current_versions = Version.objects.filter(current_version=True)
            if self.instance.pk:
                current_versions = current_versions.exclude(pk=self.instance.pk)
            if current_versions.exists():
                raise forms.ValidationError("Может быть только одна активная версия.")
        return cleaned_data


# class VersionFormset(forms.BaseInlineFormSet):
#     def clean(self):
#         super().clean()
#         count = 0
#         for form in self.forms:
#             if form.instance.indicates_current_version:
#                 count += 1
#         if count > 1:
#             raise forms.ValidationError("Может быть только 1 активная версия")