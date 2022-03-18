from django import forms


# Signup form

class SignUpForm(forms.Form):

    full_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={"class": "form-control",
                                                                                                      'placeholder': 'full name'}))

    email = forms.EmailField(label='Email', max_length=150, required=True, widget=forms.EmailInput(
        attrs={

            'class': 'form-control',
            'placeholder': 'Email',
        }
    ))
  


class LoginForm(forms.Form):
    user = forms.EmailField(required=True)
    password = forms.CharField(required=True,
                               widget=forms.PasswordInput)
