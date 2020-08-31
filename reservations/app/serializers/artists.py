from rest_framework import serializers

from app.models.artist import Artist, ArtistType, Types


class ArtistSerializer(serializers.ModelSerializer):
    """Generic model serializer on Artist."""

    class Meta:
        """Meta definition for serializer."""

        model = Artist
        fields = '__all__'
