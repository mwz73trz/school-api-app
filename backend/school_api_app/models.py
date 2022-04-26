from django.db import models

class FieldNamesMixin:
    @classmethod
    def get_field_names(cls):
        return [field.name for field in cls._meta.get_fields()]

class Student(models.Model, FieldNamesMixin):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Course(models.Model, FieldNamesMixin):
    title = models.CharField(max_length=50)
    code = models.CharField(max_length=10)
    credits = models.IntegerField()
    students = models.ManyToManyField(Student, related_name="courses", blank=True)

    def __str__(self):
        return f"{self.code} {self.title}"

