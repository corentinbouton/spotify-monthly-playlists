class Track:
	def __init__(self, name, artist, date_added, id=""):
		self.name = name
		self.artist = artist
		self.date_added = date_added
		self.id = id
  
	def print_track(self):
		print(self.name + " - " + self.artist)

class Playlist:
	list_tracks = []
	
	def __init__(self, name, id=""):
		self.name = name
		self.id = id
		
	def add_track(self, track):
		self.list_tracks.append(track)
  
	# ! à revoir : il faut passer un integer dans la méthode "pop" --> créer une fonction retournant l'entier correspondant au track
	def remove_track(self, track):
		self.list_tracks.pop(track)
  
	def print_playlist(self):
		for track in self.list_tracks:
			track.print_track()
