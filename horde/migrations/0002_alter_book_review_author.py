# Generated by Django 4.2.17 on 2025-01-04 13:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('horde', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='review_author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_reviews', to=settings.AUTH_USER_MODEL),
        ),
    ]
