from django import forms


class PlayerFilterEmailForm(forms.Form):

    email = forms.EmailField(label='Email filter ')