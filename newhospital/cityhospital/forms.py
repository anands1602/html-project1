from django import forms
from .models import Bookings

class BookingsForm(forms.ModelForm):
    class Meta:
        model = Bookings
        fields = ['p_name','p_phone','p_email','doc_name','booking_date']

        labels = {
            'p_name':'Patient Name',
            'p_phone':'phone Number',
            'p_email':'Email',
            'dep_name':'Department Name',
            'doc_name':'Doctor Name',
            'booking_date':'Booking Date'
        }