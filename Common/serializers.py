from rest_framework import serializers
from Common.models import *


class DivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Division
        fields = '__all__'


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = '__all__'


class UpazilaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upazila
        fields = '__all__'


class UnionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Union
        fields = '__all__'


class WardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ward
        fields = '__all__'


class CityCorporationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CityCorporation
        fields = '__all__'


class MunicipalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipality
        fields = '__all__'


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'
