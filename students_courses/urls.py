from django.urls import path
from .views import CourseStudentsView, CourseStudentsDeleteView


urlpatterns = [
    path("courses/<str:course_id>/students/", CourseStudentsView.as_view()),
    path(
        "courses/<str:course_id>/students/<str:student_id>/",
        CourseStudentsDeleteView.as_view(),
    ),
]
