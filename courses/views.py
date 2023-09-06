from django.shortcuts import render
from .models import Course
from .serializers import CourseSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permisions import IsAccountOwnerOrSuperuser, IsLoggedOrSuperuser
from drf_spectacular.utils import extend_schema
from throttling.throttles import CourseRateThrottle


class CourseView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsLoggedOrSuperuser]
    throttle_classes = [CourseRateThrottle]

    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    @extend_schema(
        operation_id="course_create",
        summary="Criação de cursos",
        description="Rota para cadrastar um novo curso.",
        tags=["Courses/"],
        request=CourseSerializer,
        responses={201: CourseSerializer},
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    @extend_schema(
        operation_id="courses_retrive",
        summary="Listagem de cursos",
        description="Rota para listar todos os cursos existentes.",
        tags=["Courses/"],
        responses={200: CourseSerializer},
    )
    def get(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class CourseViewDetalis(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwnerOrSuperuser]
    throttle_classes = [CourseRateThrottle]

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_url_kwarg = "course_id"

    @extend_schema(operation_id="courses_put", exclude=True)
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @extend_schema(
        operation_id="course_update",
        summary="Atualização somente dos dados de curso",
        description="Atualiza os dados de um curso passado pelo id na rota.",
        tags=["Courses/Course_id/"],
        request=CourseSerializer,
        responses={200: CourseSerializer},
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @extend_schema(
        operation_id="course_retrive",
        summary="Busca de curso por id",
        description="Busca o curso pelo id passado na rota.",
        tags=["Courses/Course_id/"],
        responses={200: CourseSerializer},
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        operation_id="course_delete",
        summary="Deleção de curso",
        description="Exclui o curso pelo id passado na rota.",
        tags=["Courses/Course_id/"],
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
