from django.urls import path
from . import views
from .views import CourseView, CourseViewDetalis

urlpatterns = [
    path("courses/", CourseView.as_view()),
    path("courses/<str:course_id>/", CourseViewDetalis.as_view()),
]
