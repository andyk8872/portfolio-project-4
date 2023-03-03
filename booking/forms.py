from .models import Booking
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
                  'total_no_group',
                  'activity_type',
                  'booking_date',)
        widgets = {
            'booking_date': DateInput(attrs={
                'min': datetime.date.today()+datetime.timedelta(days=2),
                'max': datetime.date.today()+datetime.timedelta(days=109)}),           
        }

