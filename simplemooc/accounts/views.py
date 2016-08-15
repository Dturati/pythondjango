from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, SetPasswordForm
from django.conf import settings
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, EditAccountForm, PasswordResetForm
from .utils import generate_hash_key
from .models import PasswordReset
from ..courses.models import Enrollment

def register(request):
    template_name = 'accounts/register.html'
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(
                username=user.username,
                password=form.cleaned_data['password1']
            )
            login(request,user)
            return redirect(settings.LOGIN_URL)
    else:
        form = RegisterForm()

    context = {
        'form' : form
    }

    return render(request, template_name,context)

def password_reset(request):
    User = get_user_model()
    template_name = 'accounts/password_reset.html'
    form = PasswordResetForm(request.POST or None) #não validar se estiver fazio
    context = {}
    if form.is_valid():
        form.save()
        context['success'] = True
    context['form'] = form
    return render(request, template_name, context)


def password_reset_confirm(request, key):
    template_name = 'accounts/password_reset_confirm.html'
    context = {}
    reset = get_object_or_404(PasswordReset,key=key)
    form = SetPasswordForm(user=reset.user,data=request.POST or None)
    if form.is_valid():
        form.save()
        context['success'] = True
    context['form'] = form
    return render(request, template_name, context)

#Dá permissão a usuário logado
@login_required
def dashboard(request):
    template_name = 'accounts/dashboard.html'
    context = {}
    context['Enrollments'] = Enrollment.objects.filter(user=request.user)
    return render(request, template_name,context)

@login_required
def edit(request):
    template_name = 'accounts/edit.html'
    context = {}
    if request.method == 'POST':
        form = EditAccountForm(data=request.POST,instance=request.user) #instancia que sstá sendo alterada, o model
        if form.is_valid():
            form.save()
            messages.success(request,"Alterado do com sucesso"    )
            return redirect('accounts:dashboard')
            #form = EditAccountForm(instance=request.user)
            #context['success'] = True
    else:
        form = EditAccountForm(instance=request.user)
    context['form'] = form

    return render(request, template_name,context)

@login_required
def edit_password(request):
    template_name = 'accounts/edit_password.html'
    context = {}
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST,user=request.user)
        if form.is_valid():
            form.save()
            context['success'] = form
    else:
        form = PasswordChangeForm(user=request.user)
    context['form'] = form
    return render(request,template_name,context)

