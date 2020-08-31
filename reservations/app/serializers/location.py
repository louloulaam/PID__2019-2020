from rest_framework import serializers

from app.models.location import Location


class LocationSerializer(serializers.ModelSerializer):
    """Generic model serializer on Location."""

    class Meta:
        """Meta definition for serializer."""

        model = Location
        fields = '__all__'
