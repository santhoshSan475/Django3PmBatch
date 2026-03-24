from django.shortcuts import render,redirect
from .models import CustomerModel
from .forms import customerForm
from django.http import HttpResponse
# Create your views here.

def customerInfo(request):
    customer = CustomerModel.objects.all()
    return render(request,"modelApp/customerTable.html",{"customer":customer})



def registerForm(request):
    if request.method =="POST":
        form = customerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Information")
        return HttpResponse("<p>Invalid credentials</p>")
    form = customerForm
    return render(request,"modelApp/registerModel.html",{"form":form})



def updateTableForm(request,id):
    customerData = CustomerModel.objects.get(id=id)
    if request.method =="POST":
        form = customerForm(request.POST,instance=customerData)
        if form.is_valid():
            form.save()
            return redirect("Information")
        return HttpResponse("<p>Invalid credentials</p>")
    form = customerForm
    return render(request, "modelApp/registerModel.html", {"form": form})


def deleteTableForm(request,id):
    customerData = CustomerModel.objects.get(id=id)
    customerData.delete()
    return redirect("Information")

