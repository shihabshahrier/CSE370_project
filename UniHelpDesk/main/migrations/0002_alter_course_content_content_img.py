# Generated by Django 4.1.4 on 2022-12-20 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course_content',
            name='content_img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
