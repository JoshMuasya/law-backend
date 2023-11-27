# Generated by Django 4.2.6 on 2023-11-14 05:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cases', '0002_remove_case_lawyer_name_case_lawyer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='lawyer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cases', to=settings.AUTH_USER_MODEL, to_field='username'),
        ),
    ]
