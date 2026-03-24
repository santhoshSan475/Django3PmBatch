from django.urls import path
from . import views
urlpatterns = [
   path("home/",views.HomeContent,name="homePage"),
   path("about/",views.aboutContent,name="aboutPage")
]