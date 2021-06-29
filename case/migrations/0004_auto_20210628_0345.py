# Generated by Django 3.1.2 on 2021-06-28 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('case', '0003_clientcase_case_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientcase',
            name='case_type',
            field=models.CharField(choices=[('ГР', 'Гражданское'), ('УГ', 'Уголовное')], max_length=300),
        ),
        migrations.AlterField(
            model_name='clientcase',
            name='service_type',
            field=models.CharField(choices=[('К', 'Консультация'), ('У', 'Учасите')], max_length=300),
        ),
    ]