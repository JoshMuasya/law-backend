# Generated by Django 4.2.6 on 2023-11-18 08:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0004_rename_case_description_case_case_desc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='case',
            name='case_desc',
        ),
        migrations.RemoveField(
            model_name='case',
            name='case_logged',
        ),
        migrations.RemoveField(
            model_name='case',
            name='case_number',
        ),
        migrations.RemoveField(
            model_name='case',
            name='next_hearing',
        ),
        migrations.AddField(
            model_name='case',
            name='caseName',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='case',
            name='caseNo',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='case',
            name='court',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='case',
            name='department',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='case',
            name='location',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='case',
            name='status',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='case',
            name='summary',
            field=models.TextField(default=''),
        ),
        migrations.CreateModel(
            name='CaseDates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hearing_date_original', models.DateField()),
                ('hearing_date_updated', models.DateField()),
                ('judgement_date_original', models.DateField()),
                ('judgement_date_updated', models.DateField()),
                ('submission_date_original', models.DateField()),
                ('submission_date_updated', models.DateField()),
                ('mention_date_original', models.DateField()),
                ('mention_date_updated', models.DateField()),
                ('update_timestamp', models.DateTimeField(auto_now_add=True)),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cases.case')),
            ],
        ),
    ]
