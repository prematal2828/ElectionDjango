from rest_framework import serializers
from Election.models import *


class ElectionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElectionType
        # exclude = ['created_by', 'created_at', 'updated_by', 'updated_at', 'is_deleted', 'deleted_by', 'deleted_at']
        fields = '__all__'


class ElectionCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElectionCenter
        # exclude = ['created_by', 'created_at', 'updated_by', 'updated_at', 'is_deleted', 'deleted_by', 'deleted_at']
        fields = '__all__'


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


class ElectionDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElectionInfo
        fields = '__all__'

    total_votes_in_this_election = serializers.IntegerField(read_only=True)
