from django import forms
from django.contrib.auth.models import User
from .models import AccountProfile


class ProfileForm(forms.ModelForm):
    shipping_address = forms.CharField(max_length=255, required=False)
    phone_number = forms.CharField(max_length=15, required=False)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.get("instance")
        super().__init__(*args, **kwargs)

        # Load profile data if it exists
        try:
            profile = self.user.accountprofile
            self.fields["shipping_address"].initial = profile.shipping_address
            self.fields["phone_number"].initial = profile.phone_number
        except AccountProfile.DoesNotExist:
            pass

    def save(self, commit=True):
        user = super().save(commit=commit)

        profile, _ = AccountProfile.objects.get_or_create(user=user)
        profile.shipping_address = self.cleaned_data.get("shipping_address")
        profile.phone_number = self.cleaned_data.get("phone_number")
        profile.save()

        return user

