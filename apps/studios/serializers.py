from rest_framework import serializers


class AddressSerializer(serializers.Serializer):
    address = serializers.CharField(max_length=256)


class StudioSerializer(serializers.Serializer):
    address = AddressSerializer()
    capacity = serializers.IntegerField()
