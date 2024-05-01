import sys

from modules.functions import create_monthly_playlists, get_liked_playlist, get_playlists, init_client, upload_monthly_playlists

def main(username):
	scopes = 'user-library-read playlist-modify-public'
	clt = init_client(scopes)

	liked_playlist = get_liked_playlist(clt)

	playlists = get_playlists(clt, username)

	monthly_playlists = create_monthly_playlists(liked_playlist, playlists)

	n_playlists, n_tracks = upload_monthly_playlists(clt, monthly_playlists, playlists)

	print(f'Added {n_playlists} playlists and {n_tracks} tracks.')

if __name__ == '__main__':
	if len(sys.argv) != 2:
		raise ValueError('Username not specified. Please provide a username as input.')
	username = sys.argv[1]
	if not isinstance(username, str):
		raise ValueError('Username must be a string.')
	main(username)
