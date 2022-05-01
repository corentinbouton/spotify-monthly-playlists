from fonctions import get_liked_playlist, get_playlists, initialisation, month_number_to_name

def main():
	scopes = "user-library-read"
	clt = initialisation(scopes)
	
	liked_playlist = get_liked_playlist(clt)
	#liked_playlist.print_playlist()

	playlists = get_playlists(clt)

	print(month_number_to_name(int(liked_playlist.list_tracks[0].date_added[5:7])))

if __name__ == "__main__":
	main()