from rest_framework import serializers
from .models import Artist, Song, Album, Track


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('title',)

    def to_representation(self, value):
        return f'{value.title}'


class TrackSerializer(serializers.ModelSerializer):
    song = SongSerializer(read_only=True)

    class Meta:
        model = Track
        fields = ('track_number', 'song')


class AlbumSerializer(serializers.ModelSerializer):
    tracks = TrackSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = ('year', 'tracks')


class ArtistSerializer(serializers.ModelSerializer):
    albums = AlbumSerializer(many=True, read_only=True)

    class Meta:
        model = Artist
        fields = ('name', 'albums',)
