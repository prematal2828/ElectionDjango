from rest_framework import serializers
from Common.models import *


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class DivisionSerializer(serializers.ModelSerializer):
    country_details = CountrySerializer(required=False, read_only=True)

    class Meta:
        model = Division
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        # Pop the trigger from kwargs, default to False if not provided
        include_country = kwargs.pop('include_country', False)

        # Call the parent class's __init__ method
        super(DivisionSerializer, self).__init__(*args, **kwargs)

        # Conditionally include or exclude country_details based on the trigger
        if not include_country:
            self.fields.pop('country_details')


class DistrictSerializer(serializers.ModelSerializer):
    division_details = DivisionSerializer(required=False, read_only=True)

    class Meta:
        model = District
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        include_division = kwargs.pop('include_division', False)

        super(DistrictSerializer, self).__init__(*args, **kwargs)

        if not include_division:
            self.fields.pop('division_details')


class UpazilaSerializer(serializers.ModelSerializer):
    district_details = DistrictSerializer(required=False, read_only=True)

    class Meta:
        model = Upazila
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        include_district = kwargs.pop('include_district', False)

        super(UpazilaSerializer, self).__init__(*args, **kwargs)

        if not include_district:
            self.fields.pop('district_details')


class UnionSerializer(serializers.ModelSerializer):
    upazila_details = UpazilaSerializer(required=False, read_only=True)

    class Meta:
        model = Union
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        include_upazila = kwargs.pop('include_upazila', False)

        # Call the parent class's __init__ method
        super(UnionSerializer, self).__init__(*args, **kwargs)

        if not include_upazila:
            self.fields.pop('upazila_details')


class WardSerializer(serializers.ModelSerializer):
    union_details = UnionSerializer(required=False, read_only=True)

    class Meta:
        model = Ward
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        include_union = kwargs.pop('include_union', False)

        super(WardSerializer, self).__init__(*args, **kwargs)

        if not include_union:
            self.fields.pop('union_details')


class CityCorporationSerializer(serializers.ModelSerializer):
    division_details = DivisionSerializer(required=False, read_only=True)

    class Meta:
        model = CityCorporation
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        include_division = kwargs.pop('include_division', False)

        super(CityCorporationSerializer, self).__init__(*args, **kwargs)

        if not include_division:
            self.fields.pop('division_details')


class MunicipalitySerializer(serializers.ModelSerializer):
    district_details = DistrictSerializer(required=False, read_only=True)

    class Meta:
        model = Municipality
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        include_district = kwargs.pop('include_district', False)

        super(MunicipalitySerializer, self).__init__(*args, **kwargs)

        if not include_district:
            self.fields.pop('district_details')


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'
