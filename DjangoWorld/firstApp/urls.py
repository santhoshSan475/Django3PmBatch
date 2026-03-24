from django.urls import path
from . import views


urlpatterns = [
    path("welcome/",views.welcomeScript,name="firstCode"),
    path("template/",views.templateView,name="tamizh"),
    path("studentInfo/",views.studentInfo,name="studentData"),
    path("index/<str:name>/<int:age>/",views.indexPage,name="indexInfo"),
    path("home/<str:name>/<int:age>/",views.homePage,name="homeInfo"),
    path("myTemplate/",views.myFirstTemplate,name="templateApp"),
    path("secondTemp/",views.secondTemplate,name="second"),
    path("employee/",views.employeeInfo,name="emp"),
]