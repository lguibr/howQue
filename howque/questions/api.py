from questions.models import Question
from rest_framework import viewsets, permissions
from .serializer import QuestionSerializer

# Question Viewset (like a implicit crud)

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = QuestionSerializer