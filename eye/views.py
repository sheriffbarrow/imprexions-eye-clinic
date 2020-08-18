from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'eye/index.html')


def about(request):
    return render(request, 'eye/about2.html')


def appointment(request):
    return render(request, 'eye/appointment.html')
