from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CourseViewset, UnitViewset, TopicViewSet

router = DefaultRouter()
router.register('course', CourseViewset)
router.register('unit', UnitViewset)
router.register('topic', TopicViewSet)

urlpatterns = [
    path('', include(router.urls)),
]