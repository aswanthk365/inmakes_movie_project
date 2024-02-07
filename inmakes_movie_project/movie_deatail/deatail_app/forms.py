from django import forms
from . models import movies
class update_form(forms.ModelForm):
    class Meta:
        model=movies
        fields=['name','year','discription','movie_image']
