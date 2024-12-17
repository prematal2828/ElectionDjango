from rest_framework import serializers
from Election.models import *


class ElectionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElectionType
        fields = '__all__'


class ElectionCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElectionCenter
        fields = '__all__'


class ElectionInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElectionInfo
        fields = '__all__'


class ElectionDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElectionData
        fields = '__all__'
