# Generated by Django 4.0.5 on 2022-08-24 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Image', '0008_alter_detectedimagefile_image_alter_imagefile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detectedimagefile',
            name='image',
            field=models.ImageField(blank=True, default='media/default-image.jpg', null=True, upload_to='detected_image'),
        ),
    ]