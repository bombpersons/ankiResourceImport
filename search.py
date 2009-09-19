# -*- coding: utf-8 -*-
import sys, os, codecs

class Search:
	#init all variables we need
	def __init__(self):
		#search terms
		self.terms = []
		
		#delimiters
		self.delimiters = [u"。", u".", u"？", u"?", u"！", u"!", u"\n\r", u"\n", u"\r", u"\t"]
		
		#sentences found
		self.sentences = []
		self.raw_sentences = []
		
		return
	
	#take input (from file)
	def input_from_file(self, filename):
		#open the file
		self.file = codecs.open(filename, "r", "utf-8")
		
		#read the entire file
		self.data = self.file.read()
		#now we can close the file
		self.file.close()
		
		return
	
	#adds a term to search for
	def input_search_term(self, term):
		#add the term
		self.terms.append(term)
		
		return
	
	#set the output filename
	def set_output_file(self, filename):
		self.output_filename = filename
	
	#helper functions for search
	#splits file into sentences
	def split(self):
		#use str.partition instead of split, since it keeps the delimiters.
		sentencesLeft = True
		foundAPartition = False
		tempLen = 0
		data = self.data
		while sentencesLeft:
			#loop through delimiters
			for delimiter in self.delimiters:
				#Check if this sentence is shorter than the last
				temp = data.partition(delimiter)

				if len(temp[0] + temp[1]) < tempLen or not foundAPartition:
					tempLen = len(temp[0] + temp[1])
					addSentence = (temp[0] + temp[1]).strip("\n")
					addSentence = addSentence.strip("\r")
					addSentence = addSentence.strip("\n\r")
					addSentence = addSentence.strip("\t")
					addSentence = addSentence.strip()
					tempData = temp[2]

				
				#if this is true, we found a sentence
				if temp[1] != "" and temp[2] != "":
					foundAPartition = True
			
			#if we still haven't found a sentence, then there are none left =(
			if not foundAPartition:
				sentencesLeft = False
				break
			else:
				#now add the sentence to self.raw_sentences
				#don't add if the sentence is blank
				self.raw_sentences.append(addSentence)
				data = tempData
				
				#reset the foundAPartition
				foundAPartition = False
	
	#Searchs for the terms and exports them to a file.
	def search(self):
		#search through all the sentences and see if they contain the search terms.
		for sentence in self.raw_sentences:
			Found = False
			#go through search terms
			for term in self.terms:
				#append the sentence to self.sentences if it contains the term
				if sentence.find(term) != -1 and not Found:
					#we found one
					self.sentences.append(sentence)
					Found = True
		
		return
		
	#write output
	def write_output_to_file(self):
		#open output file
		self.output_file = codecs.open(self.output_filename, "w", "utf-8")
		
		#now write each sentence with a new line in between
		print("******************************************************")
		for sentence in self.sentences:
			print(sentence)
			self.output_file.write((sentence + "\n"))
			
		#okay, done
		
		return
