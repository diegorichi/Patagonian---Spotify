import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

import sys
import click
import math

from patagonian import settings
import os
import django
os.environ["DJANGO_SETTINGS_MODULE"] = 'patagonian.settings'
django.setup()
from songs.models import Artist, Url, Song


def process_tracks(results_ar):
    for track in results_ar['tracks']['items']:
        try:

            track.pop('album')
            track.pop('available_markets')
            track.pop('external_ids')
            track.pop('popularity')

            artists_data = track.pop('artists')
            url_data = track.pop('external_urls')
            url_s, created = Url.objects.get_or_create(**url_data)
            track['external_urls'] = url_s
            song, created = Song.objects.get_or_create(
                id=track['id'], defaults=track)
            for art in artists_data:
                url_data_ar = art.pop('external_urls')
                url_ar, created = Url.objects.get_or_create(**url_data_ar)
                art['external_urls'] = url_ar
                artist, created = Artist.objects.get_or_create(
                    id=art['id'], defaults=art)
                song.artists.add(artist)
            song.save()
            print("{song_name} added".format(song_name=song.name))

        except Exception as e:
            print(e)


"""
click.option('-u', prompt='Nombre de usuario:',help='Se obtiene al ingresar a odoo. Por defecto admin')
click.option('-p', prompt='Password:',help='normalmente en openerp-server.conf. Por defecto admin')
click.option('-f', help='Nombre del archivo')

"""
@click.command()
# @click.option('-u', envvar='SPOTIPY_CLIENT_ID', help='Spotify Client ID')
# @click.option('-s', envvar='SPOTIPY_CLIENT_SECRET', help='Spotify Client Secret')
@click.option('-i', required=True, help='comma separated id list of artists')
@click.option('-udb', default='patagonian', help='DB User')
@click.option('-pdb', default='PataSongs123_', help='DB Password')
@click.option('-p', default=3306, help='DB Port')
@click.option('-h', default='patagonian1.c3hldx0oqqnn.us-east-1.rds.amazonaws.com', help='DB host')
def import_ids(i, udb, pdb, p, h):
    """
    Here are some artists IDs:

    Sebastian Yatra 07YUOmWljBTXwIseAUd9TW

    Soda Stereo 7An4yvF7hDYDolN4m5zKBp

    Eric Clapton 6PAt558ZEZl0DmdXlnjMgD

    The Beatles 3WrFJ7ztbogyGnTHbHJFl2

    Weezer 3jOstUTkEu2JkjvRdBA5Gu

    Parameter example: -i 7An4yvF7hDYDolN4m5zKBp,7An4yvF7hDYDolN4m5zKBp,3WrFJ7ztbogyGnTHbHJFl2

    Remember you need yo have environments variables:

    SPOTIPY_CLIENT_ID
    SPOTIPY_CLIENT_SECRET

    """


    try:

        artist_ids = i.replace('spotify:', '').replace(
            'artist:', '').replace(' ', '')

        sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials())

        results = sp.artists(artist_ids.split(','))

        # ver detalle
        # https://developer.spotify.com/documentation/web-api/reference/search/search/

        for ar in results.get('artists'):
            try:
                results_ar = sp.search(q=ar.get('name'), type='track', limit=50)
                process_tracks(results_ar)
                iter = math.ceil(
                    results_ar['tracks']['total'] / results_ar['tracks']['limit'])

                for index in range(iter):
                    results_ar = sp.next(results_ar['tracks'])
                    process_tracks(results_ar)

                print('fin')
            except Exception as e:
                print(e)
                pass
    except Exception as e:
        print(str(e))

if __name__ == '__main__':
    import_ids()
