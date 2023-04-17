from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import QuizViewset, QuestionViewset, AnswerViewset

router = DefaultRouter()
router.register('quiz', QuizViewset)
router.register('question', QuestionViewset)
router.register('answer', AnswerViewset)

urlpatterns = [
    path('', include(router.urls))
]
