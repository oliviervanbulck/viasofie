from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'ViaSofie/index.html', {})


def about(request):
    return render(request, 'ViaSofie/about.html', {})


def contact(request):
    return render(request, 'ViaSofie/contact.html', {})


def services(request):
    return render(request, 'ViaSofie/services.html', {})

