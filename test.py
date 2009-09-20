from ankiUpload import ankiUpload

if __name__ == "__main__":
	uploader = ankiUpload()
	uploader.sentence_field.update({
		'subs2srs': 'Expression',
	})
	
	uploader.load("deck.anki")
	
	uploader.username = "test"
	uploader.password = "test"
	
	uploader.upload()
