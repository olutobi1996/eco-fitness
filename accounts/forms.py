from django import forms
from django.contrib.auth.models import User
from .models import AccountProfile
from django_countries.widgets import CountrySelectWidget
from django_countries.fields import CountryField

class ProfileForm(forms.ModelForm):
    shipping_address = forms.CharField(max_length=255, required=False)
    phone_number = forms.CharField(max_length=15, required=False)

    default_country = CountryField(blank_label="(select country)").formfield(
        required=False, widget=CountrySelectWidget()
    )
    default_postcode = forms.CharField(max_length=20, required=False)
    default_town_or_city = forms.CharField(max_length=40, required=False)
    default_street_address1 = forms.CharField(max_length=80, required=False)
    default_street_address2 = forms.CharField(max_length=80, required=False)
    default_county = forms.CharField(max_length=80, required=False)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.get("instance")
        super().__init__(*args, **kwargs)

        try:
            profile = self.user.accountprofile
            self.fields["shipping_address"].initial = profile.shipping_address
            self.fields["phone_number"].initial = profile.phone_number
            self.fields["default_country"].initial = profile.default_country
            self.fields["default_postcode"].initial = profile.default_postcode
            self.fields["default_town_or_city"].initial = profile.default_town_or_city
            self.fields["default_street_address1"].initial = profile.default_street_address1
            self.fields["default_street_address2"].initial = profile.default_street_address2
            self.fields["default_county"].initial = profile.default_county
        except AccountProfile.DoesNotExist:
            pass

    def save(self, commit=True):
        user = super().save(commit=commit)

        profile, _ = AccountProfile.objects.get_or_create(user=user)
        profile.shipping_address = self.cleaned_data.get("shipping_address")
        profile.phone_number = self.cleaned_data.get("phone_number")
        profile.default_country = self.cleaned_data.get("default_country")
        profile.default_postcode = self.cleaned_data.get("default_postcode")
        profile.default_town_or_city = self.cleaned_data.get("default_town_or_city")
        profile.default_street_address1 = self.cleaned_data.get("default_street_address1")
        profile.default_street_address2 = self.cleaned_data.get("default_street_address2")
        profile.default_county = self.cleaned_data.get("default_county")
        profile.save()

        return user

