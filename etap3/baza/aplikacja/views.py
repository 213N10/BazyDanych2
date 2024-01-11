from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Wojewodztwa


def index(request):
    wojeweodztwa = Wojewodztwa.objects.all()
    context = {
        'wojeweodztwa' : wojeweodztwa,
    }

    return render(request, 'index.html')

def test(request):
    return HttpResponse("Logowanie")

