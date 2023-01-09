from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return render(request, 'celik/index.html')

def cookies(request):
    return render(request, 'celik/cookies/cookies.html')

# Picles
def pikles(request):
    return render(request, 'celik/picles/pikles.html')

def red_onion(request):
    return render(request, 'celik/picles/red-onion.html')

def docs_index(request):
    return render(request, 'celik/docs/index.html')

def docs_gs_required_apps(request):
    return render(request, 'celik/docs/gs/required-apps.html')

