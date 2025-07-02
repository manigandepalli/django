from rest_framework import serializers

from .models import Person, Color


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ["id"]


class PersonSerializer(serializers.ModelSerializer):
    color = ColorSerializer(read_only=True)
    # color_id = serializers.PrimaryKeyRelatedField(
    #     queryset=Color.objects.all(),
    #     source='color'
    # )

    class Meta:
        model = Person
        fields = ['id', 'name', 'age', 'color']



