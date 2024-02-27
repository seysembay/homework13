from django.urls import path
from .views import index, CourseList

urlpatterns = [
    path('courses/', index, name='courses-index'),
    path('api/courses/', CourseList.as_view(), name='courses-get')
]
