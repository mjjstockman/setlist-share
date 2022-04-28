from django.shortcuts import render
from .models import Setlist
# Create your views here.

def get_setlists(request):
    setlists = Setlist.objects.all()
    context = {
        'setlists': setlists
    }
    return render(request, 'setlist/setlists.html', context)