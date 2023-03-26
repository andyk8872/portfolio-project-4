from .models import Booking, Review
from django import forms
import datetime


class DateInput(forms.DateInput):

    input_type = 'date'


class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields = ('forename',
                  'surname',
                  'email',
                  'phone',
                  'total_no_group',
                  'activity_type',
                  'booking_date',)
        widgets = {
            'booking_date': DateInput(attrs={
                'required': True,
                'min': datetime.date.today()+datetime.timedelta(days=2),
                'max': datetime.date.today()+datetime.timedelta(days=60)}),
            'email': forms.EmailInput(attrs={
                'required': True}),
            'forename': forms.TextInput(attrs={
                'required': True,
            })
                }


class ContactForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea)


class ReviewForm(forms.ModelForm):
    """
    Presents the form for placing a review
    to the user.
    """
    class Meta:
        model = Review
        fields = ('review',)
