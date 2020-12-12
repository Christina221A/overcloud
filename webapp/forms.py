from django import forms


class CartForm(forms.Form):
    username = forms.CharField(label="username", max_length=128,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="password", max_length=256,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))
