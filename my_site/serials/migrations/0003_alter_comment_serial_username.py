# Generated by Django 4.2.5 on 2023-11-01 14:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('serials', '0002_rename_comment_comment_serial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment_serial',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_name_serial', to=settings.AUTH_USER_MODEL),
        ),
    ]