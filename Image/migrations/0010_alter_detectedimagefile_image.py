# Generated by Django 4.0.5 on 2022-08-24 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Image', '0009_alter_detectedimagefile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detectedimagefile',
            name='image',
            field=models.ImageField(default='media/default-image.jpg', null=True, upload_to='detected_image'),
        ),
    ]
