from django.shortcuts import render
from .models import Setlist
from .forms import SetlistForm
# Create your views here.

def get_setlists(request):
    setlists = Setlist.objects.all()
    # form = SetlistForm()
    context = {
        'setlists': setlists,
        # 'form': form
    }
    return render(request, 'setlist/setlists.html', context)



def add(request):
    # setlists = Setlist.objects.all()
    form = SetlistForm()
    context = {
        # 'setlists': setlists,
        'form': form
    }
    return render(request, 'setlist/add.html', context)