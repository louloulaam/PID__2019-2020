from rest_framework import serializers

from app.models.show import Representation


class RepresentationSerializer(serializers.ModelSerializer):
    """Generic model serializer on Representation."""

    class Meta:
        """Meta definition for serializer."""

        model = Representation
        fields = '__all__'
