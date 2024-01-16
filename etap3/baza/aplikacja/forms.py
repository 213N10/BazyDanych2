from django import forms


class searchWoj(forms.Form):
    szukana_nazwa = forms.CharField(label="podaj nazwe wojewodztwa")
    
    

class searchPow(forms.Form):
    szukana_nazwa = forms.CharField(label="podaj nazwe powiatu")
    

class searchGmi(forms.Form):
    szukana_nazwa = forms.CharField(label="podaj nazwe gminy")
   
    