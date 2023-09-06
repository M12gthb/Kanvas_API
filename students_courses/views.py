from django.shortcuts import render
from courses.models import Course
from courses.serializers import CourseSerializer, CourseDetailSerializer
from accounts.models import Account
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsSuperuser
from rest_framework.generics import RetrieveUpdateAPIView, DestroyAPIView
from django.shortcuts import get_object_or_404
from rest_framework import exceptions
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema


class CourseStudentsView(RetrieveUpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsSuperuser]

    queryset = Course.objects.all()
    serializer_class = CourseDetailSerializer
    lookup_url_kwarg = "course_id"

    @extend_schema(operation_id="students_courses_update", exclude=True)
    def patch(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @extend_schema(
        operation_id="student_course_register",
        summary="Adição de alunos ao curso",
        description="Adiciona alunos novos ao curso passado pelo id na rota.",
        tags=["Courses/Course_id/Students/"],
        request=CourseDetailSerializer,
        responses={200: CourseDetailSerializer},
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @extend_schema(
        operation_id="students_courses_retrive",
        summary="Listagem dos estudantes do curso",
        description="Lista todos os alunos do curso passado pelo id na rota.",
        tags=["Courses/Course_id/Students/"],
        request=CourseDetailSerializer,
        responses={200: CourseDetailSerializer},
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class CourseStudentsDeleteView(DestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperuser]

    queryset = Course.objects.all()
    serializer_class = CourseDetailSerializer
    lookup_url_kwarg = "course_id"

    def perform_destroy(self, instance):
        student = get_object_or_404(Account, pk=self.kwargs["student_id"])
        course_students = instance.students.all()
        if student not in course_students:
            raise exceptions.NotFound(
                {"detail": "this id is not associated with this course."}
            )
        instance.students.remove(student)

    @extend_schema(
        operation_id="student_course_delete",
        summary="Remoção de estudante do curso",
        description="Remove um aluno do curso passado pelo id na rota.",
        tags=["Courses/Course_id/Students/Student_id"],
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
