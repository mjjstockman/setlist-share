from django.shortcuts import render, HttpResponse

# Create your views here.
def say_hi(request):
    return HttpResponse('Hiiiiiiiiii!!!')