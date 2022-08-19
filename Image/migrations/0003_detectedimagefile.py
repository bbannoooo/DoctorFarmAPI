# Generated by Django 4.0.5 on 2022-08-19 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Image', '0002_alter_imagefile_options_remove_imagefile_title_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetectedImageFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.ImageField(upload_to='detected')),
                ('uploaded_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'detected_image',
                'ordering': ['-uploaded_at'],
            },
        ),
    ]
