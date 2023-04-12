from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CourseViewSet , UnitViewSet , TopicViewSet

router = DefaultRouter()
router.register('Course', CourseViewSet)
router.register('Topics',TopicViewSet)
router.register('Units' ,UnitViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
urlpatterns.extend(router.urls)