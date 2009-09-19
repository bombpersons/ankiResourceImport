from ankiUpload import ankiUpload

if __name__ == "__main__":
	uploader = ankiUpload()
	uploader.sentence_field.update({
		'TextProd': 'Sentence',
	})
	
	uploader.load("deck.anki")
	
	uploader.username = "admin"
	uploader.password = "admin"
	
	uploader.upload()
