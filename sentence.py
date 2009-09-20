# A class to store information about sentences
# E.g The sentence itself, media information etc

class Sentence:
	def __init__(self, sentence="", media=[], language=""):
		# Initiate variables
		self.sentence = sentence # Blank sentence to begin with.
		self.media = media # A list of media associated with this sentence.
		self.language = language # The language this sentence is in.
