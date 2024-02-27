from django.shortcuts import render
from rest_framework import generics
from .models import Course
from .serializers import CourseSerializer


def index(request):
    return render(request, "index.html")


class CourseList(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
