from django import forms
from django.forms import ModelForm

from .models import *

class MuallifModelForm(ModelForm):
    class Meta:
        model = Muallif
        fields = '__all__'
# class MuallifForm(forms.Form):
#     ismi = forms.CharField(max_length=30, label="Muallifning ismini kiriting")
#     tiri = forms.BooleanField(required=False, label="Muallif tirikmi:")
#     kitob_son = forms.IntegerField(label="Muallifning kitoblari soni:", min_value=0, max_value=15)
#     tugilgan_yi = forms.DateField(label="Muallif Tug'igan sanasi:")



class TalabaForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class KitobModelForm(ModelForm):
    class Meta:
        model = Kitob
        fields = '__all__'

class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = '__all__'