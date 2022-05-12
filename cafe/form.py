from bootstrap_datepicker_plus.widgets import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput
from django import forms
from dataclasses import Field
from importlib.metadata import files
from pyexpat import model
from django import forms

from .models import Reserve

class ApplyForm(forms.ModelForm):
    class Meta:
        model = Reserve
        fields = ['name','email', 'message', 'date', 'time','nperson']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'تكرما ادخل الاسم هنا'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'type':'Email'}),
            'message': forms.Textarea(attrs={'class': 'form-control','rows':'5'}),
            'date': DatePickerInput(options={
                    "format": "MM/DD/YYYY",
                    "locale": "en-sa",
                    # "showClose": True,
                    # "showClear": True,
                    # "showTodayButton": True,
                },
                attrs={'class': 'form-control'},).start_of('event days'),
            'time': TimePickerInput(attrs={'class': 'form-control'}).start_of('party time'),
            'nperson': forms.TextInput(attrs={'class': 'form-control'}),
            
        }
        # def __init__(self,*args, **kwargs):
        #     super(self, Reserve).__init__(*args,**kwargs)
            
        #     self.fields['name'].widget.atter['class']= 'form-control'
        #     self.fields['name'].widget.atter['placeholder']= 'Please Enter your name here'
