from fonctions import create_monthly_playlists, get_liked_playlist, get_playlists, init_client, upload_monthly_playlists

def main():
	scopes = "user-library-read playlist-modify-public"
	clt = init_client(scopes)
	
	liked_playlist = get_liked_playlist(clt)

	playlists = get_playlists(clt)

	monthly_playlists = create_monthly_playlists(liked_playlist, playlists)

	n_playlists, n_tracks = upload_monthly_playlists(clt, monthly_playlists, playlists)

	print(f"Added {n_playlists} playlists and {n_tracks} tracks.")

if __name__ == "__main__":
	main()
