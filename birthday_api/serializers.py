from rest_framework import serializers
from birthday_api.models import Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        # fields = ['name', 'age', 'image']
        fields = '__all__'
