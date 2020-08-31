from django import forms
from app.models.show import Representation
from django.forms import DateTimeField

class RepresentationForm(forms.ModelForm):
    """ Representation Form """

    """ Meta class for the RepresentationForm """
    class Meta:
        model = Representation
        fields = ['show', 'location', 'time', 'total_seats']
