from django.shortcuts import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from apps.models.models import Event

# Create your views here

def index(request):
    return HttpResponse('Hello From the Home Route')


@api_view(['GET'])
def choices(request):
    return Response(Event.SIZE)