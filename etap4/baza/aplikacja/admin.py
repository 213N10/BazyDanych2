from django.contrib import admin
from .models import Wojewodztwa, Powiaty, Gminy
# Register your models here.


admin.site.register(Gminy)
admin.site.register(Powiaty)
admin.site.register(Wojewodztwa)