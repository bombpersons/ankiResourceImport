from xml import sax

# This file contains an xml content handler used to parse the custom xml 
# and html contained in the fields in an anki deck.

class AnkiContentHandler(sax.ContentHandler):
	# This function is called when an opening tag is found
	def startElement(self, name, attrs):
		#We're ignoring this for the moment
		pass
		
	# This function is in the middle of a tag
	def characters(self, content):
		#Get the data ignoring all tags
		self.data += content
	
	def endElement(self, name):
		#Ignoring for the moment
		pass
