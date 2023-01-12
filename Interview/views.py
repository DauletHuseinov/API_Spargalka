from django.shortcuts import render
from .models import Category, QuestionAnswer
from .serializers import CategorySerializer, QuestionAnswerSerializer
from rest_framework import viewsets, generics
from rest_framework.pagination import PageNumberPagination
from django_filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


# Create your views here.

class QuestionAnswerPagination(PageNumberPagination):
    page_size = 3


class CategoryAPIView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class QuestionAnswerAPIView(viewsets.ModelViewSet):
    queryset = QuestionAnswer.objects.all()
    serializer_class = QuestionAnswerSerializer
    ordering_fields = ['-importance']
    pagination_class = QuestionAnswerPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'question']





