from rest_framework import serializers
from Election.models import *


class ElectionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElectionType
        exclude = ['created_by', 'created_at', 'updated_by', 'updated_at', 'is_deleted', 'deleted_by', 'deleted_at']


class ElectionCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElectionCenter
        exclude = ['created_by', 'created_at', 'updated_by', 'updated_at', 'is_deleted', 'deleted_by', 'deleted_at']


class ElectionInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElectionInfo
        exclude = ['created_by', 'created_at', 'updated_by', 'updated_at', 'is_deleted', 'deleted_by', 'deleted_at']


class ElectionDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElectionData
        exclude = ['created_by', 'created_at', 'updated_by', 'updated_at', 'is_deleted', 'deleted_by', 'deleted_at']


class ElectionDetailSerializer(serializers.Serializer):
    election = serializers.CharField()
    total_votes = serializers.IntegerField()

