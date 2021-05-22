from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    diction = {}
    return render(request, 'lenus_app/home.html',context =diction)

def ambu(request):
    diction ={}
    return render(request, 'lenus_app/ambu.html', context=diction)


def blood(request):
    diction ={}
    return render(request, 'lenus_app/blood.html', context=diction)


def doc(request):
    diction ={}
    return render(request, 'lenus_app/doc.html', context=diction)

def fire_ser(request):
    diction ={}
    return render(request, 'lenus_app/fire_ser.html', context=diction)

def medi(request):
    diction ={}
    return render(request, 'lenus_app/medi.html', context=diction)

def others(request):
    diction ={}
    return render(request, 'lenus_app/others.html', context=diction)

def physio(request):
    diction ={}
    return render(request, 'lenus_app/physio.html', context=diction)

def police(request):
    diction ={}
    return render(request, 'lenus_app/police.html', context=diction)

def services(request):
    diction ={}
    return render(request, 'lenus_app/services.html', context=diction)

def volun(request):
    diction ={}
    return render(request, 'lenus_app/volun.html', context=diction)


def contact(request):
    diction ={}
    return render(request, 'lenus_app/contact.html', context=diction)

