from ankiUpload import ankiUpload

if __name__ == "__main__":
	uploader = ankiUpload()
	uploader.sentence_field.update({
		'Basic': 'Front',
	})
	
	uploader.load("deck.anki")
	
	uploader.username = "test"
	uploader.password = "test"
	
	uploader.upload(media=True)
