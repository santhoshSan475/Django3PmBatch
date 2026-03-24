from django.shortcuts import render
from .forms import sampleForm

# Create your views here.


def registerForm(request):
    return render(request,"formApp/registerData.html")


def responseForm(request):
    television = int(request.GET.get("television"))
    Fridge = int(request.GET.get("Fridge"))
    MobilePhone = int(request.GET.get("Mobile Phone"))
    Ac = int(request.GET.get("Air conditionar"))
    Fan = int(request.GET.get("Fan"))
    laptop = int(request.GET.get("laptop"))
    speakers = int(request.GET.get("speakers"))
    total = television + Fridge + MobilePhone + Ac + Fan + laptop + speakers
    return render(request,"formApp/responseData.html",{"amount":total})



def sampleFormTemplate(request):
    form = sampleForm
    return render(request,"formApp/form.html",{"form":form})