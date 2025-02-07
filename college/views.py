from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from college.models import Notice, Student
from college.serializer import NoticeSerializer, StudentSerializer

# Create your views here.


class NoticeViewSet(viewsets.ModelViewSet):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


    
