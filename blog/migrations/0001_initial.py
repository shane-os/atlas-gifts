# Generated by Django 3.2.8 on 2022-04-01 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('created_by', models.CharField(max_length=25)),
                ('body', models.TextField()),
                ('posted_date', models.DateTimeField(auto_now_add=True)),
                ('categories', models.ManyToManyField(related_name='posts', to='blog.Category')),
            ],
        ),
    ]
