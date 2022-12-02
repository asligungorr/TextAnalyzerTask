from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import re
import string
from collections import Counter

# Defining a HTTP request Handler class
class ServiceHandler(BaseHTTPRequestHandler):

	# POST method definition
	def do_POST(self):
		# Only care /analyze url
		# Other options are Forbidden (403)
		if None != re.search('/analyze', self.path):
			length = int(self.headers['Content-Length'])		
			content = self.rfile.read(length)
			data = json.loads(content)

			# Each json request have to text keyword
			# Other options are Bad Request (400)
			if("text" in data):
				inputText = data["text"]
			else:
				self.send_response(400, 'Bad Request: Need text parameter')
				self.send_header('Content-Type', 'application/json')
				self.end_headers()
				return

			searchParameters = ""

			### BONUS
			# analysis keyword in a json request is optional
			if("analysis" in data):
				searchParameters = data["analysis"]

			# Letter Count - output parameter
			letters = len(inputText)

			# Remove all punctuations, only care words
			inputText = inputText.translate(inputText.maketrans('', '', string.punctuation))

			# Split seperate words and sort them based on length
			splittedInputText = inputText.split()
			sortedInputText = sorted(splittedInputText, key=len)
			
			totalLetterCount = 0;
			for str in sortedInputText:
				totalLetterCount+=len(str)
			
			# Word Count - output parameter
			wordCount = len(splittedInputText)

			### BONUS
			# Elements are already sorted based on lengths
			# Median(middle element) can be different with respect to list size
			# If list size is even, then median is arithmetic mean of the two middle values
			# If list size is odd, then median is middle number
			# MedianWordLength - output parameter
			if wordCount%2==0:
				medianWordLength = (len(sortedInputText[int(wordCount/2)]) + len(sortedInputText[int(wordCount/2-1)]))/2
			else :
				medianWordLength = len(sortedInputText[int(wordCount/2-1)])

			### BONUS
			# If list size is even, I concatenate middle words
			# MedianWord - output parameter
			if wordCount%2==0:
				medianWord = (sortedInputText[int(wordCount/2-1)] + " " + sortedInputText[int(wordCount/2)])
			else :
				medianWord = sortedInputText[int(wordCount/2-1)]

			# Number of longest element may be more than one. Therefore I return all words have max length
			# Longest - output parameter
			maxLen = len(sortedInputText[int(wordCount)-1])
			longest = []
			for i in range(len(sortedInputText)-1,-1,-1):
				if len(sortedInputText[i])!=maxLen:
					break
				longest.append(sortedInputText[i])

			# AvgLength - output parameter
			avgLength = totalLetterCount/wordCount

			# Duration - output parameter
			# TODO - There is no exact definition about it. I declared as static value
			duration = 47

			### BONUS
			# Language - output parameter
			language = self.findLanguage(splittedInputText)

			### BONUS
			# Find most common N words and theirs counts, (N is 5)
			# CommonWords - output parameter
			commonWords = self.findMostNCommonWords(splittedInputText, 5);
			
			### BONUS
			# analysis url path or json parameter handling
			# Only print listed parameter values
			if "?analysis=" in self.path or len(searchParameters)>0:
				if(len(searchParameters)>0):
					parameters = searchParameters
				else:	
					params = self.path.split("=")
					parameters = params[1].split(",")
				responseDict = {}
				for str in parameters:
					match str:
						case "wordCount":
							responseDict[str]=wordCount
						case "letters":
							responseDict[str]=letters
						case "longest":
							responseDict[str]=longest
						case "avgLength":
							responseDict[str]=avgLength
						case "medianWordLength":
							responseDict[str]=medianWordLength
						case "medianWord":
							responseDict[str]=medianWord
						case "commonWords":
							responseDict[str]=commonWords
						case "language":
							responseDict[str]=language
			else: # Print all parameters
				responseDict = {'wordCount':wordCount, 'letters':letters, 'longest':longest, 
				'avgLength': avgLength, 'duration': duration, 
				'medianWordLength':medianWordLength, 'medianWord':medianWord, 
				'commonWords':commonWords, 'language':language}
			# Convert list to json object
			jsonString = json.dumps(responseDict, indent=4)

			# Successful, return json object as response with OK (200)
			self.send_response(200)
			self.send_header('Content-Type', 'application/json')
			self.end_headers()
			self.wfile.write(jsonString.encode(encoding='utf_8'))
		else:
			self.send_response(403)
			self.send_header('Content-Type', 'application/json')
			self.end_headers()
	
	### BONUS
	# I googled commonly used words in both language
	# If the text contains one language words more then other then I returned it
	# This approach is not correct, there are external libraries to detect language.
	# But it gives us mostly correct result.
	def findLanguage(self, splittedInputText):
		mostUsedEnglishWords = ["the", "be", "to", "of", "and", "a", "in", "that", "have", "I", "it", "for", "not", "on", "with", "he", "as", "you", "do", "at", "this", "but", "his", "by", "from", "they", "we", "say", "her", "she", "or", "an", "will", "my", "one", "all", "would", "there", "their", "what", "so", "up", "out", "if", "about", "who", "get", "which", "go", "me", "when", "make", "can", "like", "time", "no", "just", "him", "know", "take", "people", "into", "year", "your", "good", "some", "could", "them", "see", "other", "than", "then", "now", "look", "only", "come", "its", "over", "think", "also", "back", "after", "use", "two", "how", "our", "work", "first", "well", "way", "even", "new", "want", "because", "any", "these", "give", "day", "most", "us"]
		mostUsedTurkishWords = ["bir", "bu", "ne", "ve", "mi", "için", "çok", "ben", "o", "de", "evet", "var", "ama", "mı", "değil", "da", "hayır", "sen", "şey", "daha", "bana", "kadar", "seni", "beni", "iyi", "tamam", "onu", "bunu", "gibi", "yok", "benim", "her", "sana", "ki", "sadece", "neden", "burada", "senin", "ya", "zaman", "hiç", "şimdi", "nasıl", "sonra", "olduğunu", "en", "mu", "misin", "hadi", "şu", "öyle", "güzel", "biraz", "musun", "önce", "İyi", "lütfen", "ona", "bak", "böyle", "oldu", "hey", "istiyorum", "geri", "onun", "bile", "gerçekten", "artık", "kim", "eğer", "bay", "yani", "çünkü", "biliyorum", "DOĞRU", "büyük", "buraya", "peki", "başka", "belki", "tanrım", "olarak", "tek", "efendim", "biri", "haydi", "olur", "et", "olacak", "olan", "adam", "İşte", "merhaba", "sanırım", "teşekkürler", "orada", "nerede", "biz", "demek", "hiçbir"]
		englishCounter = 0
		for str in splittedInputText:
			if str in mostUsedEnglishWords:
				englishCounter = englishCounter+1

		turkishCounter = 0
		for str in splittedInputText:
			if str in mostUsedTurkishWords:
				turkishCounter = turkishCounter+1

		if englishCounter>=turkishCounter:
			language = "en"
		else:
			language = "tr"
		return language

	### BONUS
	# Find most common N words and returns theirs occurrence count
	def findMostNCommonWords(self, splittedInputText, N):
		cc = Counter(splittedInputText)
		mostOccured = cc.most_common(N)
		return mostOccured

#Server Initialization
server = HTTPServer(('localhost',8080), ServiceHandler)
server.serve_forever()