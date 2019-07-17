from rest_framework import serializers
from questions.models import Question

# Question serializer
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'