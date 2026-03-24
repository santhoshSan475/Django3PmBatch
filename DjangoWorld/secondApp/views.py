from django.shortcuts import render

# Create your views here.


def HomeContent(request):
    info = {
        "name":"Harris Jayaraj",
        "description":"This is a description for the card. More details can go here.",
        "title":"Bio"
    }
    return render(request,"secondApp/home.html",{"info":info})


def aboutContent(request):
    return render(request,"secondApp/about.html")