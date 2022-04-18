import spotipy
from spotipy.oauth2 import SpotifyOAuth
import secrets

id = secrets.id
secret = secrets.secret
uri = secrets.uri
scope = secrets.scope
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=id,
                                               client_secret=secret,
                                               redirect_uri=uri,
                                               scope=scope))

def search_song(string):
    return sp.search(string, type='track', limit=1, )['tracks']['items'][0]['external_urls']['spotify']

def process_command(sentence:str):
    words = sentence.split(' ')
    command = words[0]
    q = ' '.join(str(e) for e in words[1:])

    return [command, q]

