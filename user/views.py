from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.cache import cache
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404

from user.models import Staff


def redirect_by_role(request, role):
    if role == 'AM':
        return HttpResponseRedirect('/administrator')
    elif role == 'EP':
        return HttpResponseRedirect('/employee')


def login_site(request):
    if request.method == 'GET':
        if not request.user.is_authenticated:
            # next_url = request.GET.get('next', None)
            # cache.set('next', next_url)
            # if next_url:
            #     context = {
            #         'msg': 'Ingresa tus credenciales para poder acceder'
            #     }
            #     return render(request, 'user/login.html', context)
            # else:
            return render(request, 'user/login.html', {})
        else:
            return redirect_by_role(request, get_object_or_404(Staff, user=request.user).role)
    elif request.method == 'POST':
        user = request.POST.get('user', False)
        password = request.POST.get('password', False)
        user = authenticate(username=user, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # verificar si hay una ruta siguiente
                # next_url = cache.get('next')
                # if next_url:
                #     cache.delete('next')
                # return HttpResponseRedirect(next_url)
                # else:
                role = Staff.objects.get(user=user)
                return redirect_by_role(request, role.role)
        else:
            context = {
                'msg': 'Tus credenciales no se encuentran en nuestros registros'
            }
            return render(request, 'user/login.html', context)


def logout_site(request):
    logout(request)
    return HttpResponseRedirect('/')
