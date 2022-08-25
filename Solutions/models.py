from django.db import models

# Create your models here.
class Solutions(models.Model):
    solution_id = models.IntegerField()
    solution_default = models.TextField()

    class Meta:
        db_table = 'solutions'