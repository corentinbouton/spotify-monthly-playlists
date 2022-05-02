import spotipy
from spotipy.oauth2 import SpotifyOAuth
from API_Keys import CLIENT_ID, CLIENT_SECRET
from classes import Track, Playlist
import datetime
import locale

REDIRECT_URI = 'http://localhost:8080' # URI from the my personal Spotify App

def init_client(scopes):
	"""Initializes a client with certain scopes to access the Spotify API

	Args:
		scopes (string): Scopes from the Spotify API to be passed like : "scope1 scope2 ..."

	Returns:
		Spotify: A client granting the specified access by the scopes
	"""
	return spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scopes, client_id=CLIENT_ID, client_secret=CLIENT_SECRET,redirect_uri=REDIRECT_URI))

def get_liked_playlist(clt):
	"""Calls the Spotify API to return a Playlist of all my liked tracks

	Args:
		clt (Spotify): A client granted reading access

	Returns:
		Playlist: Playlist of all my liked tracks
	"""
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
	"""Calls the spotify API to get all of my Playlists

	Args:
		clt (Spotify): A client granting reading access

	Returns:
		list: List of all my Playlists
	"""
	total = clt.user_playlists("corentin.btn", limit=1)['total']
	
	offset = 0
	idx = 0
	playlists = []

	while idx < total:
		result = clt.user_playlists("corentin.btn", limit=50, offset=offset)
		
		for pls in result['items']:
			idx += 1
			playlists.append(Playlist(pls['name'], pls['tracks']['total'], id=pls['id']))
		offset += 50

	return playlists

def month_number_to_name(number):
	"""Returns the french name of a month trough its number

	Args:
		number (string): The number of the month

	Returns:
		string: Name of the month in french
	"""
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

	return months[int(number)-1]

def get_monthly_name(track):
	"""Returns the name of the monthly Playlist associated to the creation date of a track as "Mois Année"

	Args:
		track (Track): A Track

	Returns:
		string: Name of the monthly Playlist
	"""
	return month_number_to_name(track.date_added[5:7]) + " " + track.date_added[:4]

def playlist_exists(playlist_name, playlists):
	"""Checks if a Playlist already exists in my Spotify database

	Args:
		playlist_name (string): Name of the Playlist to check
		playlists (list): List of all my Playlists

	Returns:
		bool: True if it already exists, False otherwise
	"""
	for ply in playlists:
		if playlist_name == ply.name:
			return True
	return False

def create_monthly_playlists(liked_playlist, playlists):
	"""Returns a list of monthly Playlists to add if they do not already exist

	Args:
		liked_playlist (Playlist): Playlist of all my liked tracks
		playlists (list): List of all all my Playlists

	Returns:
		list: List of monthly Playlists
	"""
	monthly_playlists = []

	i = liked_playlist.total-1

	while i >= 0:
		playlist_name = get_monthly_name(liked_playlist.tracks[i])

		if not playlist_exists(playlist_name, playlists):
			current_playlist = Playlist(playlist_name)
			while get_monthly_name(liked_playlist.tracks[i]) == playlist_name and i >= 0:
				current_playlist.add_track(liked_playlist.tracks[i])
				i -= 1
			monthly_playlists.append(current_playlist)
		else:
			i -= 1

	return monthly_playlists

def get_playlist_id(clt, name):
	"""Returns the a playlist's ID using an API call (through the get_playlists function)

	Args:
		clt (Spotify): A client
		name (string): Name of the playlist you are looking for

	Returns:
		string: The playlist's ID
	"""
	playlists = get_playlists(clt)

	for pls in playlists:
		if pls.name == name:
			return pls.id
		else:
			return -1

def upload_monthly_playlists(clt, monthly_playlists, playlists):
	"""Creates the monthly Playlists on my Spotify account

	Args:
		clt (Spotify): A client
		monthly_playlists (list): List of my monthly Playlists
		playlists (list): List of the current Playlists on my account

	Returns:
		_type_: _description_
	"""
	n_playlists = 0
	n_tracks = 0

	for pls in monthly_playlists:
		if not playlist_exists(pls.name, playlists):
			clt.user_playlist_create("corentin.btn", pls.name)
			n_playlists += 1

			# ID gathering sequence
			pid = get_playlist_id(clt, pls.name)
			if pid != -1:
				pls.id = pid
			else:
				print(f"An error occured creating the playlist {pls.name}!")
				exit()

			tracks_ids = []
			for i in range(len(pls.tracks)-1, -1, -1):
				tracks_ids.append(pls.tracks[i].id)
			clt.playlist_add_items(pls.id, tracks_ids)
			n_tracks += 1

	return n_playlists, n_tracks
