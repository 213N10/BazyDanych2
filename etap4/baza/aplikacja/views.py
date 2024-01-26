from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.http import HttpResponse
from .models import Wojewodztwa, Powiaty, Gminy
from .forms import searchWoj, searchPow, searchGmi, createWoj, createPow, createGmi, editDeleteWoj, editDeletePow, \
    editDeleteGmi


def index(request):
    return render(request, 'index.html')

def test(request):
    return HttpResponse("Logowanie")

def wyszukajAll(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        
        if action == 'Wyszukaj Województwa':
            return redirect('search_woj')  
        elif action == 'Wyszukaj Gminy':
            return redirect('search_gmi')  
        elif action == 'Wyszukaj Powiaty':
            return redirect('search_pow')  
    return render(request, 'aplikacja/wyszukaj-all.html')

def adminDanychMain(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        
        if action == 'Województwo':
            return redirect('edycja_woj')  
        elif action == 'Powiat':
            return redirect('edycja_powiat')  
        elif action == 'Gmina':
            return redirect('edycja_gmina')  
        elif action == 'Wyszukaj':
            return redirect('wyszukaj_all')
        elif action == 'logout':
            return redirect('logout')
    return render(request, 'adminDanych/admin-danych-main.html')

def edycjaGmina(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        
        if action == 'Dodaj Gminę':
            return redirect('create_gmi')  
        if action == 'Wyświetl Listę Gmin':
            return redirect('display_gmi')  
    return render(request, 'aplikacja/gmina/edycja-gmina.html')

def edycjaPowiat(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        
        if action == 'Dodaj Powiat':
            return redirect('create_pow')  
        if action == 'Wyświetl Listę Powiatów':
            return redirect('display_pow')  
    return render(request, 'aplikacja/pow/edycja-powiat.html')

def edycjaWoj(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        
        if action == 'Dodaj Województwo':
            return redirect('create_woj')  
        if action == 'Wyświetl Listę Województw':
            return redirect('display_woj')  
    return render(request, 'aplikacja/woj/edycja-woj.html')

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

def createWojew(request):
    if request.method == 'POST':
        form = createWoj(request.POST)
        if form.is_valid():
            form.save()
            wojewodztwo = form.save()  # Save the form and get the instance
            return redirect('show_woj', woj_id=wojewodztwo.id_terytowe)
    else:
        form = createWoj()

    return render(request, 'aplikacja/woj/create-woj.html', {'form': form})

def displayWojew(request):
    wojewodztwa = Wojewodztwa.objects.all()
    return render(request, 'aplikacja/woj/display-woj.html', {'wojewodztwa': wojewodztwa})

# views.py

def updateWojew(request, woj_id):
    wojewodztwo = get_object_or_404(Wojewodztwa, pk=woj_id)

    if request.method == 'POST':
        form = editDeleteWoj(request.POST, instance=wojewodztwo)

        if form.is_valid():
            action = request.POST.get('action')

            if action == 'delete':
                wojewodztwo.delete()
                return redirect('display_woj')  # Redirect to a success page after deletion

            elif action == 'save':
                form.save()
                return redirect('display_woj')  # Redirect to a success page after saving

    else:
        form = editDeleteWoj(instance=wojewodztwo)

    return render(request, 'aplikacja/woj/update-woj.html', {'form': form, 'woj_id':woj_id})


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

def createPowiat(request):
    if request.method == 'POST':
        form = createPow(request.POST)
        if form.is_valid():
            form.save()
            powiat = form.save()  # Save the form and get the instance
            return redirect('show_pow', woj_id=powiat.id_terytowe)
    else:
        form = createPow()

    return render(request, 'aplikacja/pow/create-pow.html', {'form': form})

def displayPowiat(request):
    powiaty = Powiaty.objects.all()
    return render(request, 'aplikacja/pow/display-pow.html', {'powiaty': powiaty})

# views.py

def updatePowiat(request, woj_id):
    powiat = get_object_or_404(Powiaty, pk=woj_id)

    if request.method == 'POST':
        form = editDeletePow(request.POST, instance=powiat)

        if form.is_valid():
            action = request.POST.get('action')

            if action == 'delete':
                powiat.delete()
                return redirect('display_pow')  # Redirect to a success page after deletion

            elif action == 'save':
                form.save()
                return redirect('display_pow')  # Redirect to a success page after saving

    else:
        form = editDeletePow(instance=powiat)

    return render(request, 'aplikacja/pow/update-pow.html', {'form': form, 'woj_id':woj_id})

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

def createGmina(request):
    if request.method == 'POST':
        form = createGmi(request.POST)
        if form.is_valid():
            form.save()
            gmina = form.save()  # Save the form and get the instance
            return redirect('show_gmi', woj_id=gmina.id_terytowe)  # XD wszędzie jest woj_id
    else:
        form = createGmi()

    return render(request, 'aplikacja/gmina/create-gmina.html', {'form': form})

def displayGmina(request):
    gminy = Gminy.objects.all()
    return render(request, 'aplikacja/gmina/display-gmi.html', {'gminy': gminy})

# views.py

def updateGmina(request, woj_id):
    gmina = get_object_or_404(Gminy, pk=woj_id)

    if request.method == 'POST':
        form = editDeleteGmi(request.POST, instance=gmina)

        if form.is_valid():
            action = request.POST.get('action')

            if action == 'delete':
                gmina.delete()
                return redirect('display_gmi')  # Redirect to a success page after deletion

            elif action == 'save':
                form.save()
                return redirect('display_gmi')  # Redirect to a success page after saving

    else:
        form = editDeleteGmi(instance=gmina)

    return render(request, 'aplikacja/gmina/update-gmi.html', {'form': form, 'woj_id':woj_id})