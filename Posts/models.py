from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Post(models.Model):
    id = models.BigAutoField(help_text="Post ID", primary_key=True)

    title = models.CharField(help_text="Post title", max_length=100, blank=False, null=False)


class PostContents(models.Model):
    id = models.BigAutoField(help_text="PostContents ID", primary_key=True)
    post_id = models.ForeignKey("Post", related_name="post", on_delete=models.CASCADE, db_column="post_id")
    contents = models.TextField(help_text="PostContents text", blank=False, null=False)
    detected_image = models.ImageField(upload_to='detected_images')
    solution_image = models.ImageField(upload_to='solution_images', blank=True, null=True)
    solution_contents = models.TextField(help_text="PostContents text", blank=True, null=True)