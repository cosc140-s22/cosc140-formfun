from django import forms
from django.core.validators import MaxValueValidator, MinLengthValidator, RegexValidator
from .models import WordBank


class MyForm(forms.Form):
    one = forms.CharField(label="x", required=False, validators=[MinLengthValidator(3)])
    two = forms.IntegerField(label="y", required=True, validators=[MaxValueValidator(0)])
    three = forms.EmailField(label="z", required=False) 
  #, validators=[RegexValidator('@colgate.edu$')])

class WordBankForm(forms.ModelForm):
    class Meta:
        model = WordBank
        fields = ['english','welsh']
