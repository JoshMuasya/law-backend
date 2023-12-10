from django.db import models
from django.conf import settings

class Case(models.Model):
    caseNo = models.CharField(max_length=255, default='')
    caseName = models.CharField(max_length=255, default='')
    department = models.CharField(max_length=255, default='')
    location = models.CharField(max_length=255, default='')
    court = models.CharField(max_length=255, default='')
    status = models.CharField(max_length=100, default='')
    summary = models.TextField(default='')
    loggedBy = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cases', to_field='username', null=True, blank=True)
    instrutions_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.caseNo


class CaseDateHistory(models.Model):
    case = models.ForeignKey(Case, related_name='date_histories', on_delete=models.CASCADE)
    date_name = models.CharField(max_length=255, default='')
    date_value = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return f"Date History for {self.case.caseNo}"
