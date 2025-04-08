from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category
from .models import Review

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]


        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'eco-friendly-input border-green rounded'



class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'rating': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 1,
                'max': 5,
                'placeholder': 'Rate from 1-5'
            }),
            'comment': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Write your review...'
            }),
        }



