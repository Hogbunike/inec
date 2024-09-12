from rest_framework import serializers
from .models import PollingUnit, AnnouncedPUResult, LGA

class PollingUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = PollingUnit
        fields = '_all_'

class AnnouncedPUResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnnouncedPUResult
        fields = '_all_'

class LGASerializer(serializers.ModelSerializer):
    class Meta:
        model = LGA
        fields = '_all_'