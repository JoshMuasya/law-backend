from django.urls import path
from .views import CaseViewSet, CaseDateHistoryViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'cases', CaseViewSet, basename='case')
router.register(r'date-histories', CaseDateHistoryViewSet, basename='date-histories')

urlpatterns = router.urls

