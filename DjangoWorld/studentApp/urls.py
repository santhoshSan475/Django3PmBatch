from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("employeesData",views.EmployeeViewModelSet,basename ="emp")


urlpatterns = [
    # path("students/",views.studentView),
    # path("students/<int:pk>/",views.studentObjectView),

    # path("students/",views.StudentObjectViewCode.as_view(),name="students"),
    # path("students/<int:pk>/",views.StudentObjectUpdateView.as_view()),
    # path("employees/",views.EmployeeViewObject.as_view()),
    # path("employees/<int:pk>/",views.EmployeeViewUpdateObject.as_view()),
     path("",include(router.urls))

]