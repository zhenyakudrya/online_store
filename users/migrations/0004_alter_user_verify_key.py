# Generated by Django 4.2 on 2024-01-28 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_verify_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='verify_key',
            field=models.IntegerField(blank=True, max_length=13, null=True, verbose_name='код подтверждения'),
        ),
    ]
