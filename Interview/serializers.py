from .models import Category, QuestionAnswer
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class QuestionAnswerSerializer(serializers.ModelSerializer):
    answer = serializers.CharField(write_only=True)

    class Meta:
        model = QuestionAnswer
        fields = '__all__'

