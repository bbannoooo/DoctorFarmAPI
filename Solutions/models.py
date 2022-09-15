from django.db import models

# Create your models here.
class Solutions(models.Model):
    code_id = models.IntegerField(blank=False)
    symptom = models.TextField()
    solution_default = models.TextField()

    # solution_id = models.IntegerField()
    # pesticide = models.CharField(max_length=100)
    # pesticide_image = models.ImageField(upload_to='pesticide_image', default='media/default-image.jpg', null=True)
    # pesticide_link = models.URLField()
    class Meta:
        db_table = 'Solutions'

class Code(models.Model):
    dist_id = models.IntegerField(blank=False)
    crop_id = models.IntegerField(blank=False)

    class Meta:
        db_table = 'Code'

class Pesticide(models.Model):
    code_id = models.IntegerField(blank=False)
    item_name = models.TextField()
    igr_content	= models.TextField()
    purpose = models.TextField()
    formulation = models.TextField()
    company = models.TextField()

    class Meta:
        db_table = 'Pesticide'
