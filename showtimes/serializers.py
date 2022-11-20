from rest_framework import serializers

from showtimes.models import Cinema


class CinemaSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255)
    city = serializers.CharField(max_length=255)
    movies = serializers.SlugRelatedField(many=True, slug_field='cinema', queryset=Cinema.objects.all())

    class Meta:
        model = Cinema
        fields = ("name", "city", "movies")