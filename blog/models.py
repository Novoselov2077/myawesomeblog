from django.db import models

# Create your models here.
class Post(models.Model):
	"""docstring for Post"""
	blog_title = models.CharField(max_length=300)
	blog_date = models.DateTimeField()
	blog_image = models.ImageField(upload_to='event_images/')
	blog_text = models.TextField(max_length=1000)
