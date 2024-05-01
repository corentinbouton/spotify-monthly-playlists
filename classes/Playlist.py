from classes import Track

class Playlist:
	def __init__(self, name: str, total: int = 0, id: int = None) -> None:
		self.name = name
		self.total = total
		self.tracks = []
		self.id = id

	def __repr__(self) -> str:
		return f'Name : {self.name}\nTotal tracks : {self.total}\nID : {self.id}'

	def add_track(self, track: Track) -> None:
		self.tracks.append(track)
		self.total += 1

	def remove_track(self, track: Track) -> None:
		for i in range(len(self.tracks)):
			if self.tracks[i].id == track.id:
				self.tracks.pop(i)
				self.total -= 1

	def print_tracks(self) -> None:
		for track in self.tracks:
			print(track)
