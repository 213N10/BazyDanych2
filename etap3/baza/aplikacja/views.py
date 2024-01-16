from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Wojewodztwa, Powiaty, Gminy
from .forms import searchWoj, searchPow, searchGmi


def index(request):
    return render(request, 'index.html')

def test(request):
    return HttpResponse("Logowanie")

def searchWojew(request):
    if request.method == 'POST':
        form = searchWoj(request.POST)
        if form.is_valid():
            nazwa = form.cleaned_data['szukana_nazwa']
            wyniki = Wojewodztwa.objects.filter(nazwa__icontains=nazwa)
            return render (request,'woj/wyniki-woj.html', {'wyniki': wyniki, 'form': form})
    else:
        form = searchWoj()
    return render(request, 'woj/wyszuk-woj.html', {'form':form}) 

def showWojew(request, woj_id):
    wojewodztwo = Wojewodztwa.objects.get(pk=woj_id)
    return render(request, 'woj/show-woj.html', {'wojewodztwo': wojewodztwo})

def searchPowiat(request):
    if request.method == 'POST':
        form = searchPow(request.POST)
        if form.is_valid():
            nazwa = form.cleaned_data['szukana_nazwa']
            wyniki = Powiaty.objects.filter(nazwa__icontains=nazwa)
            return render (request,'pow/wyniki-pow.html', {'wyniki': wyniki, 'form': form})
    else:
        form = searchPow()
    return render(request, 'pow/wyszuk-pow.html', {'form':form}) 

def showPowiat(request, woj_id):
    powiat = Powiaty.objects.get(pk=woj_id)
    return render(request, 'pow/show-pow.html', {'powiat': powiat})

def searchGmina(request):
    if request.method == 'POST':
        form = searchGmi(request.POST)
        if form.is_valid():
            nazwa = form.cleaned_data['szukana_nazwa']
            wyniki = Gminy.objects.filter(nazwa__icontains=nazwa)
            return render (request,'gmina/wyniki-gmina.html', {'wyniki': wyniki, 'form': form})
    else:
        form = searchGmi()
    return render(request, 'gmina/wyszuk-gmina.html', {'form':form}) 

def showGmina(request, woj_id):
    gmina = Gminy.objects.get(pk=woj_id)
    return render(request, 'gmina/show-gmina.html', {'gmina': gmina})