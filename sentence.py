# A class to store information about sentences
# E.g The sentence itself, media information etc

class Sentence:
	def __init__(self):
		# Initiate variables
		self.sentence = "" # Blank sentence to begin with.
		self.media = [] # A list of media associated with this sentence.
		self.language = "" # The language this sentence is in.
