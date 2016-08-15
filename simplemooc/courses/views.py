from django.shortcuts import render, get_object_or_404,redirect
from .forms import ContactCourse
from django.contrib.auth.decorators import login_required
from .models import  Courses,Enrollment
from django.contrib import messages

# Create your views here.
def index(request):
    courses = Courses.objects.all()
    template_name = 'courses/index.html'
    context = {
        'courses' : courses,
    }
    return render(request, template_name, context)

"""
def details(request,pk):
    course = get_object_or_404(Courses,pk = pk)
    context = {
        'course': course,
    }
    template_name = 'courses/details.html'
    return render(request, template_name, context)
"""
@login_required
def details(request,slug):
    course = get_object_or_404(Courses,slug = slug)
    context = {}
    if request.method == 'POST':
        form = ContactCourse(request.POST)
        if form.is_valid():
            context['is_valid'] = True
            form.send_mail(course)
            print(form.cleaned_data)
            form = ContactCourse()

    else:
        form = ContactCourse()

    context['form'] = form
    context['courses'] = course
    template_name = 'courses/details.html'
    return render(request, template_name, context)

@login_required #Força o usuário estar logado
def enrollment(request, slug):
    #objects chama o manager
    course = get_object_or_404(Courses, slug=slug)
    enrollment, created = Enrollment.objects.get_or_create(user = request.user,course = course)

    if created:
        enrollment.active()
        messages.success(request,"Você foi inscrito no curso com sucesso")
    else:
        if(enrollment.status != 0):
            messages.info(request, "Já inscrito no curso")
        else:
            messages.info(request,"Ocorreu um erro")
       #enrollment.active()

    return  redirect('accounts:dashboard')