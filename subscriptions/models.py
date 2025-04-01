from django.db import models

from django.db import models
from django.conf import settings

class Subscription(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    stripe_subscription_id = models.CharField(max_length=255, unique=True)
    stripe_price_id = models.CharField(max_length=255)  # Stores the Stripe plan price ID
    status = models.CharField(max_length=50, default="active")  # active, canceled, past_due
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.status}"

