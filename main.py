from fonctions import create_monthly_playlists, get_liked_playlist, get_playlists, init_client

def main():
	scopes = "user-library-read"
	clt = init_client(scopes)
	
	liked_playlist = get_liked_playlist(clt)

	playlists = get_playlists(clt)

	monthly_playlists = create_monthly_playlists(liked_playlist, playlists)

if __name__ == "__main__":
	main()
