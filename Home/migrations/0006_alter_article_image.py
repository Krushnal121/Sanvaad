# Generated by Django 5.0.1 on 2024-02-19 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0005_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(default='', upload_to='media/images'),
        ),
    ]
