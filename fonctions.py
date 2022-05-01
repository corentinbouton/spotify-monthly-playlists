import spotipy
from spotipy.oauth2 import SpotifyOAuth
from API_Keys import CLIENT_ID, CLIENT_SECRET
from classes import Track, Playlist
import datetime
import locale

REDIRECT_URI = 'http://localhost:8080'

def initialisation(scopes):
	clt = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scopes, client_id=CLIENT_ID, client_secret=CLIENT_SECRET,redirect_uri=REDIRECT_URI))
	return clt

def get_liked_playlist(clt):

	total = clt.current_user_saved_tracks(limit=1)['total'] # API call to get the total number of liked songs

	offset = 0
	idx = 0

	liked = Playlist("Titres likés")

	while idx < total:
		results = clt.current_user_saved_tracks(limit=50, offset=offset)
		for item in results['items']:
			idx += 1
			track_data = item['track']
			track = Track(track_data['name'], track_data['artists'][0]['name'], item['added_at'], track_data['id'])
			liked.add_track(track)
		offset += 50

	return liked

def get_playlists(clt):
	total = clt.user_playlists("corentin.btn", limit=1)['total']

	offset = 0
	idx = 0
	playlists = []

	while idx < total:
		result = clt.user_playlists("corentin.btn", limit=50, offset=offset)
		
		for pls in result['items']:
			idx += 1
			playlists.append([pls['name'], pls['id']])
		offset += 50

	return playlists

def month_number_to_name(number):
	locale.setlocale(locale.LC_ALL, "fr_FR.UTF-8")

	monthint = list(range(1,13))
	months = []
	for X in monthint:
		month = datetime.date(1900, X , 1).strftime('%B')
		new_string=""
		for i in range(len(month)):
			if i==0:
				new_string+=month[i].upper()
			else:
				new_string+=month[i]
		months.append(new_string)

	return months[number]
