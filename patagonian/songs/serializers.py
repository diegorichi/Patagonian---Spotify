from rest_framework import serializers

from .models import Song, Artist, Url


class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Url
        fields = ['spotify']


class ArtistSerializer(serializers.ModelSerializer):

    external_urls = UrlSerializer()
    class Meta:
        model = Artist
        fields = ('id', 'name', 'uri', 'href', 'type', 'external_urls')

class SongSerializer(serializers.ModelSerializer):

    artists = ArtistSerializer(
                        many=True)
    external_urls = UrlSerializer()

    class Meta:
        model = Song
        fields = ('id', 'name', 'duration_ms', 'explicit',
         'artists', 'disc_number', 'href', 'is_local',
         'is_playable', 'preview_url', 'track_number', 'type', 'uri', 'external_urls')



class ListSongSerializer(serializers.ModelSerializer):
    songId = serializers.CharField(source='id')
    songTitle  = serializers.CharField(source='name')
    artistName = serializers.StringRelatedField(source='artists__name')



    class Meta: 
        model = Song
        fields = ('songId', 'songTitle','artistName')

