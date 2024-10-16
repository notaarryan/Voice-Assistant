import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv("client_id")
client_secret = os.getenv("client_secret")

print(client_id,client_secret)

def getAlbums(a):
    results = sp.artist_albums(artistURI[a], album_type='album')
    albums = results['items']
    while results['next']:
        results = sp.next(results)
        albums.extend(results['items'])

    for album in albums:
        print(album['name'])

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id,client_secret,redirect_uri="http://localhost:1234/",scope="user-library-read"))

artistURI = {"Karan Aujla" : "spotify:artist:6DARBhWbfcS9E4yJzcliqQ", "Travis Scott" : "spotify:artist:0Y5tJX1MQlPlqiwlOH1tJY","Drake":"spotify:artist:3TVXtAsR1Inumwj472S9r4"}