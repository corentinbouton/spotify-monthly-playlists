class Track:
	def __init__(self, name, artist, date_added, id=""):
		self.name = name
		self.artist = artist
		self.date_added = date_added
		self.id = id
  
	def __repr__(self):
		return f"{self.name} - {self.artist} - {self.date_added} - {self.id}"

class Playlist:
	def __init__(self, name, total=0, id=""):
		self.name = name
		self.total = total
		self.tracks = []
		self.id = id

	def __repr__(self):
		return f"Name : {self.name}\nTotal tracks : {self.total}\nID : {self.id}"
		
	def add_track(self, track):
		self.tracks.append(track)
		self.total += 1

	def remove_track(self, track):
		for i in range(len(self.tracks)):
			if self.tracks[i].id == track.id:
				self.tracks.pop(i)
				self.total -= 1

	def print_tracks(self):
		for track in self.tracks:
			print(track)
