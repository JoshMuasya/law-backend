from rest_framework import serializers
from .models import Case, CaseDateHistory

class CaseDateHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CaseDateHistory
        fields = '__all__'

    
class CaseSerializer(serializers.ModelSerializer):
    date_histories = CaseDateHistorySerializer(many=True, read_only=True)

    class Meta:
        model = Case
        fields = '__all__'