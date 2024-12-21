# Generated by Django 4.2.17 on 2024-12-21 17:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('date_of_birth', models.DateField()),
                ('nationality', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=50)),
                ('favourite_book', models.CharField(max_length=200)),
                ('bio', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('genre', models.CharField(max_length=50)),
                ('book_published', models.DateField()),
                ('review', models.TextField()),
                ('rating', models.IntegerField(choices=[(0, '1-5'), (1, 'One Star'), (2, 'Two Star'), (3, 'Three Star'), (4, 'Four Star'), (5, 'Five Star')], default=0)),
                ('status', models.IntegerField(choices=[(0, 'Save as Draft'), (1, 'Post')], default=0)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='horde.author')),
                ('review_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='horde_books', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]