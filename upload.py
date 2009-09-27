# Import libraries we need
import os
from mechanize import Browser

from sentence import Sentence

# Don't use this class directly unless you want to inherit it to write
# Another uploader.
class Upload:
	#Init --------------------------------------------------------------
	def __init__(self):
		# Default settings
		self.login_url = "http://anki-resource.uk.to/accounts/login/"
		self.username = ""
		self.password = ""
		
		self.new_sentence_url = "http://anki-resource.uk.to/sentences/new/"
		self.use_media = False # Don't use media by default.
		self.language = "" # Language the sentences are in.
		
		# Types
		self.types = {
			'Image': ('.png', '.bmp', '.jpg', '.jpeg', '.svg'),
			'Video': ('.avi', '.mpeg', '.mpg', '.mp4', '.ogv', '.flv'),
			'Sound': ('.mp3', '.ogg', '.flac'),
		}
		
		
		# Vars used by other functions
		self.sentences = [] # Sentences to upload to the server
							# The sentence structure also contains the
							# Location of media and it's type
							
	
	#Load --------------------------------------------------------------
	# This should be overwritten when inherited.
	# Use this function to fill out self.sentences, otherwise upload()
	# Will have no data to upload.
	def load(self, filename):
		pass
	
	#Upload ------------------------------------------------------------
	# Upload the extracted data to anki-resource (you can change the
	# server to anything you want by changing upload.url)
	# 
	# If you want to upload media as well use media=True
	def upload(self, media=False):
		# Use mechanize to login and add sentences
		br = Browser()
		
		# Go to the login page
		br.open(self.login_url)
		
		# Fill in the form
		br.select_form(nr=0)
		br['username'] = self.username
		br['password'] = self.password
		
		# Login
		br.submit()
		
		# Now loop for every sentence, and post the data
		for sentence in self.sentences:
			
			# Go to add sentence page
			br.open(self.new_sentence_url)
			
			# Fill in the form
			br.select_form(nr=0)
			br['sentence'] = sentence.sentence.encode("utf-8")
			br['language'] = ['Other']
			br['other_language'] = sentence.language
			br['tags'] = sentence.tags
			
			print br['tags']
			
			#Figure out where to put uploads
			if media:
				for media in sentence.media:
					control = br.form.find_control(name=self.uploadType(media))
					control.add_file(open(media), 'multipart/form-data', media)

			
			# Submit
			br.submit()
			
	#Helpers------------------------------------------------------------
	# Helper functions 
	
	# uploadType - finds out what type of file a filename is.
	def uploadType(self, filename):
		if filename.endswith(self.types['Image']):
			return 'image'
		elif filename.endswith(self.types['Video']):
			return 'video'
		elif filename.endswith(self.types['Sound']):
			return 'sound'
			
		else:
			return ""
		
