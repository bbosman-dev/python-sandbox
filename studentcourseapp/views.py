from .models import Student, Course, StudentCourse
from django.http import HttpResponse
from rest_framework import viewsets, permissions
from .serializers import StudentSerializer, CourseSerializer, StudentCourseSerializer


def index(request):
    return HttpResponse("Dit is de student-course app.")

class StudentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows students to be viewed or edited.
    """
    queryset = Student.objects.all().order_by('last_name')
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated]

class CourseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows courses to be viewed or edited.
    """
    queryset = Course.objects.all().order_by('course_name')
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]

class StudentCourseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows studentcourses to be viewed and edited.
    """
    queryset = StudentCourse.objects.all().order_by('id')
    serializer_class = StudentCourseSerializer
    permissions_classes = [permissions.IsAuthenticated]
