from django.shortcuts import render
from django.template import loader


# Create your views here.
def index(request):
    test = "Hello world!"
    context = {
        'test': test,
        'nbar': 'panden'
    }
    return render(request, 'panden/index.html', context)
