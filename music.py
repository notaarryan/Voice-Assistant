import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="00dcbfe71cdd4c1d93787ac467149f79",
                                               client_secret="2fa81312204c4f7591046db197cf7394",
                                               redirect_uri="http://localhost:1234/",
                                               scope="user-library-read"))

artistURI = {"Karan Aujla" : "spotify:artist:6DARBhWbfcS9E4yJzcliqQ", "Travis Scott" : "spotify:artist:0Y5tJX1MQlPlqiwlOH1tJY","Drake":"spotify:artist:3TVXtAsR1Inumwj472S9r4"}