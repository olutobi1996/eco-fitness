from django.db import models


class AboutUs(models.Model):
    title = models.CharField(max_length=200, default="About Us")
    content = models.TextField(
        help_text="Content about your company, mission, values, etc."
    )
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title
