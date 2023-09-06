from django.urls import path
from .views import ContentView, ContentViewDetails


urlpatterns = [
    path("courses/<str:course_id>/contents/", ContentView.as_view()),
    path(
        "courses/<str:course_id>/contents/<str:content_id>/",
        ContentViewDetails.as_view(),
    ),
]
