from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIRequestFactory, APITestCase, force_authenticate
from django.urls import reverse

from .views import StudentViewSet
from .models import Student


class StudentTestCase(APITestCase):
    @classmethod
    def setup(self):
        Student.objects.create(first_name="Marie", last_name="Curie")
        Student.objects.create(first_name="Michelle", last_name="Curie")

    def test_not_auth_user_access_denied(self):
        """
        When user is not logged in, access is forbidden.
        """
        response = self.client.get(reverse('student-list'))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_can_view_student_list(self):
        """
        API GET students/ returns complete student list
        """
        # todo: create tests, fix bug response.status.403
        # factory = APIRequestFactory()
        # view = StudentViewSet.as_view(actions={'get': 'retrieve'})
        # user = User.objects.create_user('testuser', 'test@user.nl', 'userpassword101')
        # request = factory.get(reverse('student-list'))
        # force_authenticate(request, user=user)
        # response = view(request)
        # self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_can_view_student(self):
        """
        API GET students/{id} returns detail of student with pk={id}
        """


    def test_can_update_student(self):
        """
        API PUT students/{id} updates student record with pk={id}, returns student
        """

    def test_can_create_student(self):
        """
        API POST students/ creates new student, returns student
        """

    def test_can_delete_student(self):
        """
        API GET students/{id} deletes student with pk={id}, returns student
        """


    def test_can_view_course_list(self):
        """
        API GET courses/ returns complete course list
        """

    def test_can_view_course(self):
        """
        API GET courses/{id} returns detail of course with pk={id}
        """

    def test_can_update_course(self):
        """
        API PUT courses/{id} updates course with pk={id}, returns course
        """

    def test_can_create_course(self):
        """
        API POST courses/ creates new course, returns course
        """

    def test_can_delete_course(self):
        """
        API GET courses/{id} deletes course with pk={id}, returns course
        """


    def test_can_view_studentcourse_list(self):
        """
        API GET studentcourses/ returns complete studentcourse list
        """

    def test_can_view_studentcourse(self):
        """
        API GET studentcourses/{id} returns detail of studentcourse with pk={id}
        """

    def test_can_update_studentcourse(self):
        """
        API PUT studentcourses/{id} updates student studentcourse with pk={id}, returns studentcourse
        """

    def test_can_create_studentcourse(self):
        """
        API POST studentcourses/ creates new studentcourse, returns studentcourse
        """

    def test_can_delete_studentcourse(self):
        """
        API GET studentcourses/{id} deletes studentcourse with pk={id}, returns studentcourse
        """
