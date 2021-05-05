from django import forms

class LoadForm(forms.Form):
    story_title=forms.ChoiceField(label='Title',choices=[],widget=forms.RadioSelect)
    def __init__(self, choices=[],s_title="",*args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['story_title'].choices=choices
        s_title=s_title
    