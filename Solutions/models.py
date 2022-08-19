from django.db import models

# Create your models here.
class Solutions(models.Model):
    solution_id = models.IntegerField()
    solution_default = models.CharField(max_length=300)

    class Meta:
        db_table = 'solutions'