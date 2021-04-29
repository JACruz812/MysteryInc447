from django import forms

class LoadForm(forms.Form):
    choices=[]
    s_title=''
    def __init__(self, *args, **kwargs):
        choices=[]
        s_title=''
    s_title=forms.ChoiceField(choices=choices,widget=forms.RadioSelect)