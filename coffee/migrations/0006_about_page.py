# Generated by Django 4.1.5 on 2023-04-17 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0005_contactbox_delete_juicess'),
    ]

    operations = [
        migrations.CreateModel(
            name='about_page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tital', models.CharField(max_length=50)),
                ('about_text', models.CharField(max_length=500)),
                ('about_image', models.ImageField(max_length=250, upload_to='static/background')),
            ],
        ),
    ]
