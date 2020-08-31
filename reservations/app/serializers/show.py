from rest_framework import serializers

from app.models.show import Show


class ShowSerializer(serializers.ModelSerializer):
    """Generic model serializer on Show."""

    class Meta:
        """Meta definition for serializer."""

        model = Show
        fields = '__all__'

    def create(self, validated_data):
        show = Show(
            title = validated_data['title'],
            slug = validated_data['slug'],
            description = validated_data['description'],
            poster = validated_data['poster'],
            bookable = validated_data['bookable'],
            price = validated_data['price'],
            date_created = validated_data['date_created']
        )
        show.save()
        return show
        #return Show.objects.create(**validated_data)

class ExternalShowSerializer(serializers.ModelSerializer):
    """Generic model serializer on Show."""

    class Meta:
        """Meta definition for serializer."""

        model = Show
        exclude = ['slug', 'id']

    """ def create(self, validated_data):
        show = Show(
            title = validated_data['title'],
            description = validated_data['description'],
            poster = validated_data['poster'],
            bookable = validated_data['bookable'],
            price = validated_data['price'],
            date_created = validated_data['date_created']
        )
        show.save()
        return show
        #return Show.objects.create(**validated_data) """

