from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.http import HttpResponse
from django.contrib import messages
from django.template.loader import get_template
from django.contrib.auth.decorators import login_required
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
from django.contrib.auth import authenticate, login, logout


@login_required(login_url='login')
def index(request):
    model = Staff.objects.all()
    context = {
        'models': model
    }
    return render(request, 'dashboard/index.html', context)

@login_required(login_url='login')
def payslip(request, pk):
    model = Staff.objects.get(id=pk)
    template_path = 'dashboard/payslip.html'
    context = {
        'model': model
    }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)
    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def register(request):
    page = 'register'
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account Created Successful. You can now log in')
            return redirect('login')
    context = {
        'form': form,
        'page': page
    }
    return render(request, 'user/register_login.html', context)


def login_page(request):
    if request.user.is_authenticated:
        return redirect('/')
    
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']

        user = authenticate(request, username=username, password=password1)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Invalid Information')
            return redirect('login')
    else:
        return render(request, 'user/register_login.html', {})


def logout_page(request):
    logout(request)
    return redirect('/')
