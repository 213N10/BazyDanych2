from django import forms


class searchWoj(forms.Form):
    szukana_nazwa = forms.CharField(label="podaj nazwe wojewodztwa")
    # check this form
    