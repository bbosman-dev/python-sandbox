from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    class Meta:
        constraints = [
        models.UniqueConstraint(fields=['first_name', 'last_name'], name='unique_first_name_last_name')
        ]

class Course(models.Model):
    course_name = models.CharField(max_length=50, unique=True)
    course_information = models.TextField(blank=True)
    students = models.ManyToManyField(Student, through='StudentCourse')

    def __str__(self):
        return self.course_name


class StudentCourse(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return '%s enlisted in %s' % (self.student, self.course)
