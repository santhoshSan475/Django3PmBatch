from django.urls import path
from . import views


urlpatterns = [
    path("table/",views.customerInfo,name="Information"),
    path("registerHere/",views.registerForm,name="registration"),
    path("UpdateForm/<int:id>/",views.updateTableForm,name="valueUpdate"),
    path("deleteForm/<int:id>/",views.deleteTableForm,name="valueDelete")
]