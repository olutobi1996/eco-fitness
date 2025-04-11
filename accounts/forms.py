from django import forms
from django.contrib.auth.models import User
from .models import AccountProfile


class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(required=True)
    shipping_address = forms.CharField(max_length=255, required=False)
    phone_number = forms.CharField(max_length=15, required=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()

        # Update or create the AccountProfile linked to the user
        account_profile, created = AccountProfile.objects.get_or_create(user=user)
        account_profile.shipping_address = self.cleaned_data.get('shipping_address')
        account_profile.phone_number = self.cleaned_data.get('phone_number')
        account_profile.save()

        return user



