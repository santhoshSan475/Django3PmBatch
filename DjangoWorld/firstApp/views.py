from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.


def welcomeScript(request):
    return HttpResponse("Hello coders")


def templateView(request):
    return HttpResponse("<h1>tamilselvan is a intelligent student </h1>")



def studentInfo(request):
    studentName = """
      <html>
         <head>
            <title>Hello coders</title>
         </head>
         <body>
            <h1>Student Information</h1>
            <ul>
               <li>Jovina</li>
               <li>Female</li>
               <li>ME</li>
               <li>Python fullstack</li>
            </ul>
         </body>
      </html>
    """
    return HttpResponse(studentName)



def indexPage(request,name,age):
    return redirect("homeInfo",name=name,age=age)

def homePage(request,name,age):
    return HttpResponse(f"This is {name} and my age is {age}")


def myFirstTemplate(request):
    return render(request,"firstApp/homePage.html",context={"script":"Django Template","title":"My Document"})


def secondTemplate(request):
    myPara = " Warning : This is a development server. Do not use it in a production setting. Use a production WSGI or ASGI server instead."
    return render(request, "firstApp/secondPage.html",{"value":myPara})

def employeeInfo(request):
    employee = {
        "EmpName": "Tamilselvan",
        "EmpId" : 201234,
        "designation":"Software developer",
        "Income":"15LPA",
        "Mode" : "Remote",
        "title":"Employee Info"
    }
    return render(request,"firstApp/employeeData.html",context={"employee": employee})






