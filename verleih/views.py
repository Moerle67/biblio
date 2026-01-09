from django.http import HttpResponse
from django.shortcuts import render

from .models import Verleihung

def start(request):
    name = "Ingo Mörl und der VFB"
    h1 = "Bücher außer Haus"
    lst_buecher = Verleihung.objects.filter(bis__isnull = True)
    content = {
        'name': name,
        'h1': h1,
        'lst_buecher': lst_buecher
    }
    return render(request, 'verl_buecher.html', content)
