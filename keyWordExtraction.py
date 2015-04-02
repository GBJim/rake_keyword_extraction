import rake
extractor = rake.Rake("SmartStoplist.txt")   #it uses smartStopList, you can shoose FoxStopList instead.

def getKeywords(sentence):
	keywords = extractor.run(sentence)
	return keywords



# it returns a list which consist of tuples, each tuple represents one keyword and it's score
keywords = getKeywords("I was an adventurer like you, then I took an arrow in the knee")
print(keywords)


