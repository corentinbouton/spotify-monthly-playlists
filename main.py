import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
from API_Keys import CLIENT_ID, CLIENT_SECRET
from classes import Track, Playlist

REDIRECT_URI = 'http://localhost:8080'
scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=CLIENT_ID, client_secret=CLIENT_SECRET,redirect_uri=REDIRECT_URI))

results = sp.current_user_saved_tracks(limit=1) # API call to get the total number of liked songs

offset = 0
idx = 0

liked = Playlist("Titres likés")

while idx < results['total']:
	results = sp.current_user_saved_tracks(limit=50, offset=offset)
	for item in results['items']:
		idx += 1
		track_data = item['track']
		track = Track(track_data['name'], track_data['artists'][0]['name'], item['added_at'], track_data['id'])
		liked.add_track(track)
	offset += 50

liked.print_playlist()
