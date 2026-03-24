from django.shortcuts import render
from .models import studentModel
from django.http import Http404
from django.http import JsonResponse
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from employeeApp.models import EmployeeModel
from employeeApp.serializers import EmployeeSerializer
from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets


# Create your views here.

#manual serialization
# def studentView(request):
#     student = studentModel.objects.all()
#     student_list = list(student.values())
#     return JsonResponse(student_list,safe=False)


@api_view(["GET","POST"])
def studentView(request):
    if request.method == 'GET':
        student = studentModel.objects.all()
        serializer = StudentSerializer(student,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == "POST":
         student = StudentSerializer(data=request.data)
         if student.is_valid():
             student.save()
             return Response(student.data,status=status.HTTP_201_CREATED)
         return Response(student.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET","PUT"])
def studentObjectView(request,pk):
    try:
        student = studentModel.objects.get(pk=pk)
    except student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = StudentSerializer(student)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == "PUT":
        serializer = StudentSerializer(student,data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



class StudentObjectViewCode(APIView):
    def get(self,request):
        student = studentModel.objects.all()
        serializer = StudentSerializer(student,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)




class StudentObjectUpdateView(APIView):
    def get_object(self,pk):
        try:
            return studentModel.objects.get(pk=pk)

        except studentModel.DoesNotExist:
            raise Http404

    def get(self,request,pk):
        student = self.get_object(pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data,status=status.HTTP_302_FOUND)

    def put(self,request,pk):
        student = self.get_object(pk)
        serializer = StudentSerializer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        student = self.get_object(pk)
        student.delete()
        return Response(status=status.HTTP_202_ACCEPTED)







class EmployeeViewObject(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeSerializer

    def get(self,request):
        return self.list(request)

    def post(self,request):
        return self.create(request)


class EmployeeViewUpdateObject(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeSerializer

    def get(self,request,pk):
        return self.retrieve(request,pk=pk)

    def put(self, request,pk):
        return self.update(request,pk=pk)

    def delete(self,request,pk):
        return self.destroy(request,pk=pk)



class EmployeeViewObject(generics.ListCreateAPIView):
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeViewUpdateObject(generics.RetrieveUpdateDestroyAPIView):
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeSerializer




#

class EmployeeViewModelSet(viewsets.ViewSet):
    def list(self,request):
        employee = EmployeeModel.objects.all()
        serializer = EmployeeSerializer(employee,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


    def create(self,request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def retrieve(self,request,pk):
        employee = EmployeeModel.objects.get(pk=pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data,status=status.HTTP_302_FOUND)



class EmployeeViewModelSet(viewsets.ModelViewSet):
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeSerializer



