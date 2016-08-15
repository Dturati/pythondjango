from django import forms
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User #user do django
from django.contrib.auth import get_user_model
from .utils import generate_hash_key
from .models import PasswordReset
from .mail import send_email_template
"""
class RegisterForm(UserCreationForm):

    email = forms.EmailField(label='E-mail')

    #Cria novo metodo save que substitui o savde de UserCreationForm
    def save(self, commit=True):
        user = super(RegisterForm,self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email = email).exists():
            raise forms.ValidationError('Já existe esse email')
        return email

class EditAccountForm(forms.ModelForm):

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email = email).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError('Já existe esse email')
        return email

    class Meta:
        model = User
        fields = ['username','email','first_name','last_name']
"""
User = get_user_model()

class PasswordResetForm(forms.Form):
    email = forms.EmailField(label='E-mail')
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            return email
        raise forms.validators("Email não cadastrado")

    def save(self):
        user = User.objects.get(email=self.cleaned_data['email'])
        key = generate_hash_key(user.username)
        reset = PasswordReset(key=key, user=user)
        reset.save()
        template_name = 'accounts/password_reset_mail.html'
        subjetct = 'Criar nova senha'
        context = {
            'reset' : reset
        }
        send_email_template(subjetct,template_name,context,[user.email])

class RegisterForm(forms.ModelForm):

    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmação de senha', widget=forms.PasswordInput)

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2  and password1 != password2:
            raise forms.ValidationError('A confirmação de senhanão está correta')
        return password2


    #Cria novo metodo save que substitui o savde de UserCreationForm
    def save(self, commit=True):
        user = super(RegisterForm,self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ['username','email']

class EditAccountForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username','email','name']