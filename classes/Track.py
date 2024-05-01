from datetime import datetime

class Track:
	def __init__(self, name: str, artist: str, date_added: str, id: int = None) -> None:
		self.name = name
		self.artist = artist
		self.date_added = date_added
		self.id = id

	def __repr__(self) -> str:
		return f'{self.name} - {self.artist} - {self.date_added} - {self.id}'
