# Generated by Django 3.1.2 on 2021-06-21 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('case', '0002_auto_20210621_0257'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientcase',
            name='case_status',
            field=models.CharField(max_length=100, null=True, verbose_name='Статус дела'),
        ),
    ]