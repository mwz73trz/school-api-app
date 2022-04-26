from rest_framework import serializers
from .models import Course, Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = Student.get_field_names()


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = Course.get_field_names()