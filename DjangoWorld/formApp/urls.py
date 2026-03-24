from django.urls import path
from . import views

urlpatterns =[
   path("addData/", views.registerForm),
   path("responsePage/",views.responseForm),
   path("myForm/",views.sampleFormTemplate),
]



