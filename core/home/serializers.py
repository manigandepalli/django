from rest_framework import serializers

from .models import Person, Color


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ["color_name"]


class PersonSerializer(serializers.ModelSerializer):
    #color = ColorSerializer() disabled just for testing

    class Meta:
        model = Person
        fields = '__all__'
        #depth = 1


