# Generated by Django 4.0.5 on 2022-08-24 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Image', '0007_alter_detectedimagefile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detectedimagefile',
            name='image',
            field=models.ImageField(default='media/default-image.jpg', upload_to='detected_image'),
        ),
        migrations.AlterField(
            model_name='imagefile',
            name='image',
            field=models.ImageField(default='media/default-image.jpg', upload_to='uploads'),
        ),
    ]