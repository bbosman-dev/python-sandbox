from .models import Student, Course, StudentCourse
from rest_framework import serializers


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name']


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'course_name', 'course_information']

class StudentCourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StudentCourse
        fields = ['id', 'course_id', 'student_id']
