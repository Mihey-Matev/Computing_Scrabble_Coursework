class Node:
	#nodeCount = 0
	def __init__(self, wordA):
		#Node.nodeCount += 1
		self.nodeLetter = wordA[0]		
		self.hasArcs = False
		self.arcLetters = {}	
		self.canTerminate = False		# canTerminate is True if this path forms a valid word
		self.addArc(wordA[1:])

	
	def getCanTerminate(self, canTerminate = None):
		
		return self.canTerminate
	
		
	def getArcLetters(self, arcDict = None):	
		
		return self.arcLetters
	
	
	def isWord(self, canTerminate = None):
		
		return self.canTerminate
	
	
	def getNodeLetter(self, letter = None):
			
		return self.nodeLetter
		
		
	def addArc(self, wordA, connectToNode = None):
		if len(wordA) > 0:
			self.hasArcs = True
			
			try:
				self.arcLetters[wordA[0]].addArc(wordA[1:])		# If a path exists, uses self.startNode.addArc(reverseWord)that;
			except:				
				self.arcLetters[wordA[0]] = Node(wordA) 	# otherwise, creates a new path.
		elif connectToNode == None:
			self.canTerminate = True
		else:												# allows for non-linear connections to be made
			self.arcLetters[connectToNode.getNodeLetter()] = connectToNode
				
				
class Gaddag:	
	def __init__(self, elements):
		self.startNode = Node("*")		# this is just treated as the starting point
		
		for word in elements:
			self.addWord(word)
			
			
	def navigateToNode(self, wordA, currentNode = None):
		if currentNode == None:
			currentNode = self.startNode
		
		try:
			if len(wordA) > 0:
				return  self.navigateToNode(wordA[1:], currentNode.arcLetters[wordA[0]])
			else:
				return currentNode				# returns the node
		except:
			return None		# Node/word not found
		

	def findNodes(self, wordA, currentWord = "", currentNode = None):
		if currentNode == None:
			currentNode = self.startNode	
		nodesWordsCollection = []
		
		wordAtoP = wordA		# A = argument P = parameter
			
		for char in wordA:
			if char != "*":
				currentNode = self.navigateToNode(char, currentNode)
				currentWord += wordAtoP[0]
				wordAtoP = wordAtoP[1:]
			else:
				for charOfNode in currentNode.getArcLetters():
					nodesWordsCollection += self.findNodes(charOfNode + wordAtoP[1:], currentWord, currentNode)
				break
				
				
		if wordAtoP == "" and currentNode != None:
			return [[currentWord, currentNode]]
		else:
			return nodesWordsCollection

	
	"""def addWord(self, word):			# this is used when i need examples with a simple structure
		self.startNode.addArc(word)"""
	
	def addWord(self, word):			# this got fixed up in v4		# minimization added in v6
		reverseWord = word[::-1]	
		self.startNode.addArc(reverseWord)
															# This part creates all paths based on the anchor (first) letter that has been met.		
		wordToAdd = word[0] + "@" + word[1:]
		#print (wordToAdd)
		self.startNode.addArc(wordToAdd)
		
		nodesAfterThird = []
		if len(word) >= 3:
			theGaddagWordStart = word[0] + "@" + word[1]
			aNode = self.navigateToNode(theGaddagWordStart)
			for n in range(len(word) - 2):
				aNode = self.navigateToNode(word[n + 2], aNode)
				nodesAfterThird.append(aNode)
		for n in range(len(word) - 2):			
			n += 1
			subWordToAdd = word[n::-1] + "@"
			self.startNode.addArc(subWordToAdd, nodesAfterThird[n - 1])
			
"""	
		
someWords = ["cat", "category", "care", "careen", "car", "cats", "cars", "can", "can"]
someWords = ["car"]

myGaddag = Gaddag(someWords)

print (myGaddag.navigateToNode("").getArcLetters())
print ("\n------------------------------------------------------------------\n")
print (myGaddag.navigateToNode("c").getArcLetters())
print ("\n------------------------------------------------------------------\n")
print (myGaddag.navigateToNode("c@").getArcLetters())
print ("\n------------------------------------------------------------------\n")
print (myGaddag.navigateToNode("c@a").getArcLetters())
print ("\n------------------------------------------------------------------\n")
print (myGaddag.navigateToNode("c@at").getArcLetters())
print ("\n------------------------------------------------------------------\n")
print (myGaddag.navigateToNode("c@ate").getArcLetters())

print (Node.nodeCount)



print (myGaddag.navigateToNode("c"))
print (myGaddag.findNodes("c***s"))
for n in myGaddag.findNodes("c***s"):
	print (n[1].getNodeLetter(), n[1].getIsWord())
	
for n in myGaddag.findNodes("c**s"):			# no words exist that have this pattern; nothing expected
	print (n[1].getNodeLetter(), n[1].getIsWord())

print (myGaddag.navigateToNode("c@at").getNodeLetter())
print (myGaddag.navigateToNode("").canTerminate)

"""








































