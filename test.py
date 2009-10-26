from ankiUpload import ankiUpload

if __name__ == "__main__":
	uploader = ankiUpload()
	uploader.sentence_field.update({
		#'Basic': 'Front',
		#'TextProd': 'Sentence',
		'subs2srs': 'Expression',
	})
	
	uploader.search_tags = [u'Fairy']
	
	uploader.login_url = "http://127.0.0.1:8000/accounts/login/"
	uploader.new_sentence_url = "http://127.0.0.1:8000/sentences/new/"
	uploader.new_list_url = "http://127.0.0.1:8000/lists/newlist"
	
	uploader.list = "Fairy Tail 2"
	
	uploader.load("/home/bombpersons/Dropbox/Public/AnkiDeck/JapaneseAnki.anki")
	
	uploader.username = "admin"
	uploader.password = "admin"
	
	uploader.upload(media=True)



