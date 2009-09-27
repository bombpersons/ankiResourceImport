from ankiUpload import ankiUpload

if __name__ == "__main__":
	uploader = ankiUpload()
	uploader.sentence_field.update({
		'Basic': 'Front',
		'TextProd': 'Sentence',
		'subs2srs': 'Expression',
	})
	
	uploader.load("/home/bombpersons/Dropbox/Public/AnkiDeck/JapaneseAnki.anki")
	
	uploader.username = "admin"
	uploader.password = "admin"
	
	uploader.upload(media=True)
