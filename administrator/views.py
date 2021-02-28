from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.http import require_POST

from crud.models import Person
from user.views import allowed_area


@login_required(login_url='/')
@allowed_area('AM')
def index(request):
    return render(request, 'administrator/index.html', {})


@login_required(login_url='/')
@allowed_area('AM')
def person_list(request):
    persons = Person.objects.filter(is_active=True)
    data = {
        'persons': persons,
    }
    return render(request, 'administrator/person.html', data)


@require_POST
@login_required(login_url='/')
@allowed_area('AM')
def create_person(request):
    try:
        person = Person.objects.create(picture=request.FILES.get('picture', None),
                                       first_name=request.POST.get('first_name', None),
                                       last_name=request.POST.get('last_name', None),
                                       phone=request.POST.get('phone', None),
                                       email=request.POST.get('email', None),
                                       )
        if person:
            data = {
                'msg': 'ok',
                'person': {
                    'id': person.id,
                    'picture': person.picture.url,
                    'first_name': person.first_name,
                    'last_name': person.last_name,
                    'phone': person.phone,
                    'email': person.email,
                    'date_joined': person.date_joined.__str__(),
                }
            }
            return JsonResponse(data=data, safe=False, status=201)
        else:
            data = {
                'msg': 'error',
                'data': f'No se pudo crear la persona con nombre {request.POST.get("first_name")}'
            }
            return JsonResponse(data=data, safe=False, status=422)
    except Exception as e:
        data = {
            'msg': 'error',
            'data': f'Error: {e.__str__()}'
        }
        return JsonResponse(data=data, safe=False, status=500)
