from rest_framework import generics, viewsets
from .models import CaseDateHistory, Case
from .serializers import CaseDateHistorySerializer, CaseSerializer


class CaseViewSet(viewsets.ModelViewSet):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer


class CaseDateHistoryViewSet(viewsets.ModelViewSet):
    queryset = CaseDateHistory.objects.all()
    serializer_class = CaseDateHistorySerializer