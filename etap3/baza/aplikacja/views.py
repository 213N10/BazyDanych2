from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Wojewodztwa
from .forms import searchWoj


def index(request):
    wojewodztwa = Wojewodztwa.objects.all()
    context = {
        'wojewodztwa' : wojewodztwa,
    }

    return render(request, 'index.html')

def test(request):
    return HttpResponse("Logowanie")

def searchWojew(request):
    if request.method == 'POST':
        form = searchWoj(request.POST)
        if form.is_valid():
            nazwa = form.cleaned_data['szukana_nazwa']
            wyniki = Wojewodztwa.objects.filter(nazwa__icontains=nazwa)
            return render (request,'wyniki.html', {'wyniki': wyniki, 'form': form})
    else:
        form = searchWoj()
    return render(request, 'wyszuk-woj.html', {'form':form}) 

