class Track:
	def __init__(self, name, artist, date_added, id=""):
		self.name = name
		self.artist = artist
		self.date_added = date_added
		self.id = id
  
	def print_track(self):
		print(f"{self.name} - {self.artist} - {self.date_added} - {self.id}")

class Playlist:
	def __init__(self, name, total=0, id=""):
		self.name = name
		self.total = total
		self.tracks = []
		self.id = id
		
	def add_track(self, track):
		self.tracks.append(track)
		self.total += 1
  
	# ! à revoir : il faut passer un integer dans la méthode "pop" --> créer une fonction retournant l'entier correspondant au track
	def __remove_track(self, track):
		self.tracks.pop(track)
		self.total -= 1
  
	def print_playlist_tracks(self):
		for track in self.tracks:
			track.print_track()

	def print_playlist_info(self):
		print(f"Name : {self.name}")
		print(f"Total tracks : {self.total}")
		print(f"ID : {self.id}")

	# TODO : à implémenter
	def __upload_playlist(self):
		print()
