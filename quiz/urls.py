from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import QuizListView, QuestionListView, AnswerListView, SubmissionViewset
router = DefaultRouter()
router.register('submission', SubmissionViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('quiz/', QuizListView.as_view()),
    path('question/', QuestionListView.as_view()),
    path('answer/', AnswerListView.as_view()),
]
urlpatterns.extend(router.urls)