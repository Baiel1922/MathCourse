from django.urls import path, include
from rest_framework.routers import DefaultRouter

from group.views import GroupViewSet, GroupStudentViewSet

router = DefaultRouter()
router.register('group', GroupViewSet)
router.register('group_student', GroupStudentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
urlpatterns.extend(router.urls)