from django.db import models
from django.conf import settings
from cloudinary_storage.storage import MediaCloudinaryStorage

class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(
        upload_to='blog_images/',
        null=True,
        blank=True,
        storage=MediaCloudinaryStorage()
    )
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
