# Generated by Django 4.1.5 on 2023-04-10 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0002_juicess'),
    ]

    operations = [
        migrations.AlterField(
            model_name='juice',
            name='jyuice_image',
            field=models.ImageField(max_length=500, upload_to='static/background'),
        ),
    ]
