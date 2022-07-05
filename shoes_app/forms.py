from django import forms
from .models import Shoes, MoreInfo


class ShoesForm(forms.ModelForm):
    class Meta:
        model = Shoes
        exclude = ['more_info']


class MoreInfoForm(forms.ModelForm):
    class Meta:
        model = MoreInfo
        fields = ['condition', 'type']
