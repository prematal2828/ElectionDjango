from rest_framework import serializers

from Common.serializers import AddressSerializer
from Election.models import *


class ElectionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElectionType
        # exclude = ['created_by', 'created_at', 'updated_by', 'updated_at', 'is_deleted', 'deleted_by', 'deleted_at']
        fields = '__all__'


class ElectionCenterSerializer(serializers.ModelSerializer):
    address_details = AddressSerializer(required=False, read_only=True)

    class Meta:
        model = ElectionCenter
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        include_address = kwargs.pop('include_address', False)

        super(ElectionCenterSerializer, self).__init__(*args, **kwargs)

        if not include_address:
            self.fields.pop('address_details')


class ElectionInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElectionInfo
        # exclude = ['created_by', 'created_at', 'updated_by', 'updated_at', 'is_deleted', 'deleted_by', 'deleted_at']
        fields = '__all__'


class ElectionDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElectionData
        # exclude = ['created_by', 'created_at', 'updated_by', 'updated_at', 'is_deleted', 'deleted_by', 'deleted_at']
        fields = '__all__'


class ElectionSeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElectionSeat
        # exclude = ['created_by', 'created_at', 'updated_by', 'updated_at', 'is_deleted', 'deleted_by', 'deleted_at']
        fields = '__all__'
