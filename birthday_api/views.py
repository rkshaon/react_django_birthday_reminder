from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from birthday_api.models import Person
from birthday_api.serializers import PersonSerializer

@api_view(['GET'])
def personList(request):
    persons = Person.objects.all().order_by('-id')
    serializer = PersonSerializer(persons, many=True)
    return Response(serializer.data)
