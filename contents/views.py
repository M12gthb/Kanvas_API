from django.shortcuts import render
from .models import Content
from .serializers import Contentserializer
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsSuperuser, IsAccountOwnerOrSuperuser
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from drf_spectacular.utils import extend_schema


class ContentView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsSuperuser]
    serializer_class = Contentserializer
    lookup_url_kwarg = "course_id"

    def perform_create(self, serializer):
        serializer.save(course_id=self.kwargs["course_id"])

    @extend_schema(
        operation_id="content_create",
        summary="Criação de conteúdos e associação ao curso",
        description="Cria o conteúdo e o associa ao curso passado pelo id na rota.",
        tags=["Courses/Course_id/Contents/"],
        request=Contentserializer,
        responses={201: Contentserializer},
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class ContentViewDetails(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAccountOwnerOrSuperuser]

    queryset = Content.objects.all()
    serializer_class = Contentserializer
    lookup_url_kwarg = "content_id"

    @extend_schema(operation_id="content_put", exclude=True)
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @extend_schema(
        operation_id="content_retrive",
        summary="Busca de conteúdo por id",
        description="Busca o conteúdo do curso passado pelo id da rota.",
        tags=["Courses/Course_id/Contents/Content_id"],
        request=Contentserializer,
        responses={200: Contentserializer},
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        operation_id="content_update",
        summary="Atualização somente do conteúdo",
        description="Atualiza o conteudo de um curso passado pelo id da rota.",
        tags=["Courses/Course_id/Contents/Content_id"],
        request=Contentserializer,
        responses={200: Contentserializer},
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @extend_schema(
        operation_id="content_delete",
        summary="Deleção de conteúdos",
        description="Deleta o conteudo de um curso passado pelo id da rota.",
        tags=["Courses/Course_id/Contents/Content_id"],
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
