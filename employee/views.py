from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from user.views import allowed_area


@login_required(login_url='/')
@allowed_area(['EP'])
def index(request):
    return render(request, 'employee/index.html', {})


@login_required(login_url='/')
@allowed_area('EP')
def show_hello(request):
    return render(request, 'employee/index.html', {})
