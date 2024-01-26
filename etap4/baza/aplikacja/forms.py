from django import forms
from .models import Wojewodztwa, Powiaty, Gminy


class searchWoj(forms.Form):
    szukana_nazwa = forms.CharField(label="podaj nazwe wojewodztwa")


class searchPow(forms.Form):
    szukana_nazwa = forms.CharField(label="podaj nazwe powiatu")


class searchGmi(forms.Form):
    szukana_nazwa = forms.CharField(label="podaj nazwe gminy")


class createWoj(forms.ModelForm):
    class Meta:
        model = Wojewodztwa
        fields = '__all__'  # Use '__all__' to include all fields from the model in the form
        exclude = ['ludnosc', 'powierzchnia']


class createPow(forms.ModelForm):
    class Meta:
        model = Powiaty
        fields = '__all__'  # Use '__all__' to include all fields from the model in the form
        exclude = ['ludnosc', 'powierzchnia']


class createGmi(forms.ModelForm):
    class Meta:
        model = Gminy
        fields = '__all__'  # Use '__all__' to include all fields from the model in the form


class editDeleteWoj(forms.ModelForm):
    class Meta:
        model = Wojewodztwa
        fields = '__all__'


class editDeletePow(forms.ModelForm):
    class Meta:
        model = Powiaty
        fields = '__all__'


class editDeleteGmi(forms.ModelForm):
    class Meta:
        model = Gminy
        fields = '__all__'
