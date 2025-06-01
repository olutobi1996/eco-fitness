from django.db import models


class HeroImage(models.Model):
    title = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to="hero_images/")
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.title or f"Hero Image #{self.id}"
