from django.db import models

class Post(models.Model):
    id = models.BigAutoField(help_text="Post ID", primary_key=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    
    detected_image = models.ImageField()
    detected_class = models.IntegerField()
    detected_default_solution = models.TextField(help_text="detected_default_solution")
    detected_contents = models.TextField(help_text="PostContents text", blank=True, null=True)
    
    solution_image = models.ImageField(upload_to='solution_images', blank=True, null=True)
    solution_contents = models.TextField(blank=True, null=True)
    
    is_public = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        db_table = 'Posts'
        ordering = ['-created_at']
