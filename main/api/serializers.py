from email.policy import default

from rest_framework import serializers
from main.models import *

class FachSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=10)
    description = serializers.CharField(max_length=100)

    class Meta:
        model = Fach
        fields = '__all__'

    def create(self, validated_data):
        country_obj = Fach(**validated_data)
        country_obj.save()
        return country_obj

    def update(self, instance, validated_data):
        instance.name = validated_data["name"]
        instance.description = validated_data["description"]
        instance.save()
        return instance

class AntwortSerializer(serializers.ModelSerializer):
    fach = serializers.PrimaryKeyRelatedField(queryset=Fach.objects.all())
    choice = serializers.IntegerField(default=0)

    class Meta:
        model = Antwort
        fields = '__all__'

    def create(self, validated_data):
        country_obj = Antwort.objects.create(**validated_data)
        country_obj.save()
        return country_obj

    def update(self, instance, validated_data):
        instance.choice = validated_data.get("choice", instance.choice)
        instance.fach = validated_data.get("fach", instance.fach)
        instance.save()
        return instance