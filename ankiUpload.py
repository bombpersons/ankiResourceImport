# import upload so we can inherit the class
from upload import Upload
from search import Search
from sentence import Sentence
from ankiParse import ankiParse, strip_tags

import anki
from anki.cards import Card
from anki.facts import Fact

import os

# This class inherits upload and adds anki upload support.
class ankiUpload(Upload):
	def __init__(self):
		# Default variables that are only used in this class
		self.search_terms = [] # Empy by default (empty = don't search)
		self.sentence_field = {} # Dictionary containing which field to
								 # use as the sentence. Only fields in
								 # models in the dictionary will be used.
								 # In the form { modelname: fieldname }
								 						 
		self.tag_strip = [		# Tags to strip from tags obtained from cards.
				'Media-Missing', # Remove anki specific tags that we don't want on the site.
				'Leech',
		]
								 
		
		# Call the usual __init__ function
		Upload.__init__(self)
	
	#Load
	def load(self, filename):
		# Load the anki deck and get all the sentences
		deck = anki.DeckStorage.Deck(filename)
		
		# Grab the sentences based on which field in each model is the
		# sentence.
		
		# Cycle through models of the deck
		for model in deck.models:
			
			# First check if we know which field to use in this model
			if model.name in self.sentence_field:
				# Grab all facts ids
				fact_ids = deck.s.all("select id from facts where modelId = " + str(model.id))
				
				# Get facts from the id's
				facts = []
				for fact_id in fact_ids:
					facts.append(deck.s.query(Fact).get(fact_id[0]))
				
				# Get the sentences from the facts, and media.
				sentences = []
				parser = ankiParse()
				for fact in facts:
					# The new sentence
					newSentence = Sentence(sentence=fact[self.sentence_field[model.name]])
					media = [] # Temperory media without full path
					full_media = [] # Media with full path
					
					# Loop through fields in fact searching for media
					for field in model.fieldModels:
						parser.feed(fact[field.name])
						media.extend(parser.media)
						parser.close()
					
					# If this anki deck has a media directory add that to media path
					if deck.mediaDir() != None:					
						# Add full path to media
						del full_media[:]
						for m in media:
							#print os.path.join(deck.mediaDir(), m)
							if deck.mediaDir():
								path = deck.mediaDir
							else:
								path = ""
							
							full_media.append(os.path.join(path, m))
							
						newSentence.media = full_media
					
					# Sentence Language
					newSentence.language = self.language
					
					# Remove tags that we don't want (anki specific tags, etc)
					tags = fact.tags
					for tag in self.tag_strip:
						tags = tags.strip(tag)
					
					newSentence.tags = tags
					
					# Append the sentence	
					sentences.append(newSentence)
					
				
				# Ok, now if there are search terms search, search the
				# sentences.
				if len(self.search_terms) > 0:
					# Make a searcher
					searcher = Search()
					searcher.search_terms = self.search_terms
				
					# Put the sentences into the searcher
					for sentence in sentences:
						searcher.raw_sentences.append(sentence.sentence)
										
					# Search
					searcher.search()
					
					# Now update sentences to contain the results
					for sentence in sentences:
						if sentence.sentence not in searcher.sentences:
							sentences.remove(sentence)
					
				# Before we add these sentences, we need to strip any
				# xml / html from them
				i = 0
				for sentence in sentences:
					sentences[i].sentence = strip_tags(sentence.sentence)
					i += 1
					
				# Now add these to the 
				self.sentences.extend(sentences)
					
		# We should be done now, now everything is up to the base
		# upload function.
		deck.close()
