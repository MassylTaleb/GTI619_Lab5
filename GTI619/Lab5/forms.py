from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import *
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


class SignUpForm(forms.Form):
    alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
    passMaxLength = Params.objects.values('passMaxLength').first().popitem()[1]
    passMinLength = Params.objects.values('passMinLength').first().popitem()[1]
    needUppercase = Params.objects.values('needUppercase').first().popitem()[1]
    needLowercase = Params.objects.values('needLowercase').first().popitem()[1]
    needSpecialChar = Params.objects.values('needSpecialChar').first().popitem()[1]
    needNumericChar = Params.objects.values('needNumericChar').first().popitem()[1]
    username = forms.CharField(label='Enter Username', min_length=4, max_length=150)
    if not needSpecialChar:
        password1 = forms.CharField(label='Enter password', max_length=passMaxLength, min_length=passMinLength, validators=[alphanumeric])
        password2 = forms.CharField(label='Confirm password', max_length=passMaxLength, min_length=passMinLength, validators=[alphanumeric])
    else:
        password1 = forms.CharField(label='Enter password', max_length=passMaxLength, min_length=passMinLength)
        password2 = forms.CharField(label='Confirm password', max_length=passMaxLength, min_length=passMinLength)

    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    role = forms.ChoiceField(choices=[(tag.value, tag.value) for tag in Roles], label='Role', initial=Roles.ADMIN,
                             widget=forms.Select(), required=True)

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise ValidationError("Username already exists")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise ValidationError("Email already exists")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")

        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)


class ParamsForm(ModelForm):
    class Meta:
        model = Params
        fields = ['isPeriodicChange', 'passMinLength', 'passMaxLength', 'needUppercase', 'needLowercase',
                  'needSpecialChar', 'needNumericChar', 'cannotUsePreviousPass', 'numberOfAttemps',
                  'delayBetweenAttemps', 'contactAdminAfterFailure']

        labels = {'isPeriodicChange': 'Password must be changed periodically',
                  'passMinLength': 'Minimum length for password',
                  'passMaxLength': 'Maximum length for password',
                  'needUppercase': 'Need at least one uppercase',
                  'needLowercase': 'Need at least one lowercase',
                  'needSpecialChar': 'Need at least one special character',
                  'needNumericChar': 'Need at least one numeric character',
                  'cannotUsePreviousPass': 'User cannot re-use recent previous passwords',
                  'numberOfAttemps': 'Max number of attemps',
                  'delayBetweenAttemps': 'Delay between attemps (in minutes)',
                  'contactAdminAfterFailure': 'User must contact admin on failure'}

