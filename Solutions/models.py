from django.db import models

# Create your models here.
class Solutions(models.Model):
    solution_id = models.IntegerField()
    solution_default = models.TextField()
    # pesticide = models.CharField(max_length=100)
    # pesticide_image = models.ImageField(upload_to='pesticide_image', default='media/default-image.jpg', null=True)
    # pesticide_link = models.URLField()
    class Meta:
        db_table = 'solutions'