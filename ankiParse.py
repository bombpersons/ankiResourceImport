from HTMLParser import HTMLParser
import re

# A html parser to parse the html tags in anki fields. Helps identify
# media in an anki deck.

class ankiParse(HTMLParser):
	# Init
	def __init__(self):
		# Just need to initiate some vars
		self.media = []
		
		HTMLParser.__init__(self)
	
	# I have know idea if this will work, overide the feed() function
	# so that we can parse anki's custom sound tags ([sound:filename])
	def feed(self, data):
		# Try and find sound tag
		
		# Compile a regex expression
		p = re.compile(r"\[sound:(\w+.\w+)\]")
		
		# Search through data for a match
		matched = p.match(data)
		
		# If we found a match
		if matched != None:
			# Extract data and call handle_startendtag
			self.handle_startendtag("sound", [('src', matched.group(1))])
			
			# Now return so we don't have it be parsed again
			return
		
		# Call the usual function
		return HTMLParser.feed(self, data)
	
	# Override the function that gets called when it finds a start tag
	def handle_starttag(self, tag, attrs):
		pass
		
	# Overide the function that gets called when a single tag (i.e
	# <img />
	def handle_startendtag(self, tag, attrs):
		attrs = dict(attrs)
		# Check for a img tag
		if tag == "img":
			# Find the source image
			self.media.append(attrs['src'])
		
		# Check for video / sound tag	
		elif tag == "sound":
			# Find the source
			self.media.append(attrs['src'])
			
	# Overide close, to reset all vars
	def close(self):
		del self.media[:]
		
		HTMLParser.close(self)
		

