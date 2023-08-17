from django import forms

from app1.models import table1

class todoform(forms.ModelForm):
    class Meta:
        model=table1
        fields= ['name','priority','date']