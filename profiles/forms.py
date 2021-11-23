from django import forms


class UpdateProfileForm(forms.Form):
    FirstName = forms.CharField(max_length=30)
    LastName = forms.CharField(max_length=30)
    Username = forms.CharField(max_length=30)
    Image = forms.ImageField()
    Password = forms.CharField(widget=forms.PasswordInput, min_length=10)

