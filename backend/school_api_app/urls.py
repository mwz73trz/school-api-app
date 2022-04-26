from django.urls import path
from rest_framework import routers
from django.urls import path, include
from .views import CourseViewSet, StudentViewSet

r = routers.DefaultRouter()
r.register("students", StudentViewSet, basename="student")
r.register("courses", CourseViewSet, basename="course")


urlpatterns = [path("", include(r.urls))]