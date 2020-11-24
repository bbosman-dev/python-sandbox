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
        factory = APIRequestFactory()
        view = StudentViewSet.as_view(actions={'get': 'retrieve'})
        user = User.objects.create_user('testuser', 'test@user.nl', 'userpassword101')
        request = factory.get(reverse('student-list'))
        force_authenticate(request, user=user)
        response = view(request)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        #self.assertQuerySetEqual(response.context[], )
