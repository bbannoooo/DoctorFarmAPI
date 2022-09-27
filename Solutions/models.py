from django.db import models

# Create your models here.
class Solutions(models.Model):
    code_id = models.IntegerField(blank=False)
    symptom = models.TextField()
    solution_default = models.TextField()

    class Meta:
        db_table = 'Solutions'

class Code(models.Model):
    dist_id = models.IntegerField(blank=False)
    crop_id = models.IntegerField(blank=False)

    class Meta:
        db_table = 'Code'

class Pesticide(models.Model):
    pesticide_image = models.ImageField(upload_to='pesticide_image', null=True, blank=True)
    code_id = models.IntegerField(blank=False)
    item_name = models.TextField()
    igr_content	= models.TextField()
    purpose = models.TextField()
    formulation = models.TextField()
    company = models.TextField()

    class Meta:
        db_table = 'Pesticide'
