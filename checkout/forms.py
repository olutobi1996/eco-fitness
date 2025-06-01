from django import forms

from .models import Order


class OrderForm(forms.ModelForm):
    """Form for users to enter their checkout details"""

    class Meta:
        model = Order
        fields = (
            "full_name",
            "email",
            "phone_number",
            "country",
            "postcode",
            "town_or_city",
            "street_address1",
            "street_address2",
            "county",
        )

        widgets = {
            "full_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Full Name"}
            ),
            "email": forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "Email Address"}
            ),
            "phone_number": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Phone Number"}
            ),
            "country": forms.Select(attrs={"class": "form-control"}),
            "postcode": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Postal Code"}
            ),
            "town_or_city": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Town or City"}
            ),
            "street_address1": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Street Address 1",
                }
            ),
            "street_address2": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Street Address 2 (Optional)",
                }
            ),
            "county": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "County/State"}
            ),
        }

    def __init__(self, *args, **kwargs):
        """
        Add placeholders, remove labels, and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            "full_name": "Full Name",
            "email": "Email Address",
            "phone_number": "Phone Number",
            "postcode": "Postal Code",
            "town_or_city": "Town or City",
            "street_address1": "Street Address 1",
            "street_address2": "Street Address 2 (Optional)",
            "county": "County/State",
        }

        self.fields["full_name"].widget.attrs["autofocus"] = True
        for field in self.fields:
            if field != "country":
                self.fields[field].widget.attrs["placeholder"] = placeholders[
                    field
                ]
            self.fields[field].widget.attrs["class"] = "form-control rounded-0"
            self.fields[field].label = False
