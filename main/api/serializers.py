from email.policy import default

from rest_framework import serializers
from main.models import *

class FachSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=10)
    description = serializers.CharField(max_length=100)
    zu_niedrig = serializers.IntegerField(default=0)
    genau_richtig = serializers.IntegerField(default=0)
    zu_hoch = serializers.IntegerField(default=0)

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
        instance.zu_niedrig = validated_data["zu_niedrig"]
        instance.genau_richtig = validated_data["genau_richtig"]
        instance.zu_hoch = validated_data["zu_hoch"]
        instance.save()
        return instance