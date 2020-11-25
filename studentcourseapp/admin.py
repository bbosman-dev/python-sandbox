from django.contrib import admin

from .models import Student, Course, StudentCourse


class StudentInLine(admin.TabularInline):
    model = Student
    extra = 3

class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    ordering = ('last_name', 'first_name')
    list_filter = ['last_name']
    search_fields = ['last_name']

class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'course_information')
    ordering = ('course_name', )

class StudentCourseAdmin(admin.ModelAdmin):
    list_display = ('course', 'student')
    list_filter = ['course', 'student']

admin.site.register(Student, StudentAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(StudentCourse, StudentCourseAdmin)
