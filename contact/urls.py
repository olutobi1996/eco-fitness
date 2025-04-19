from django.urls import path
from .views import contact_view, newsletter_signup

urlpatterns = [
    path('contact/', contact_view, name='contact'),
    path('newsletter/', newsletter_signup, name='newsletter_signup'),
]



