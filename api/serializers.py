from rest_framework import serializers

from .models import Movie

class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields = ('name', 'overview', 'image_url', 'score', 'release_date')