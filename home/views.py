from django.shortcuts import render

# Create your views here.
def home(request):
    # return HttpResponse('Hiiiiiiiiii!!!')
    return render(request, 'home/index.html')