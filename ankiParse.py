from HTMLParser import HTMLParser
import re

# A html parser to parse the html tags in anki fields. Helps identify
# media in an anki deck. Can also strip html

class ankiParse(HTMLParser):
	# Init
	def __init__(self):
		# Reset 
		self.reset()
		
		# Just need to initiate some vars
		self.media = []
		
		# Vars for stripping
		self.fed = []
		
		HTMLParser.__init__(self)
			
	# Strip tags
	def handle_data(self, d):
		self.fed.append(d)
		
	def get_data(self):
		return ''.join(self.fed)
	
	# I have know idea if this will work, overide the feed() function
	# so that we can parse anki's custom sound tags ([sound:filename])
	def feed(self, data):
		# Try and find sound tag
		
		# Compile a regex expression
		p = re.compile(r"(.*)\[sound:(\w+.\w+)\](.*)")
		
		# Search through data for a match
		matched = p.match(data)
		
		# If we found a match
		if matched != None:
			# Extract data and call handle_startendtag
			self.handle_startendtag("sound", [('src', matched.group(2))])
			
			# Feed the rest of the string.
			self.feed(matched.group(1))
			self.feed(matched.group(3))
			
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
		
def strip_tags(html):
    s = ankiParse()
    s.feed(html)
    return s.get_data()

