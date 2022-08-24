from django.db import models

# Create your models here.
class ImageFile(models.Model):
    email = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='uploads', default='media/default-image.jpg')
    uploaded_at = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        db_table = 'image'
        ordering = ['-uploaded_at']

class DetectedImageFile(models.Model):
    email = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='detected_image', default='media/default-image.jpg', null=True)
    class_id = models.IntegerField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        db_table = 'detected_image'
        ordering = ['-uploaded_at']
