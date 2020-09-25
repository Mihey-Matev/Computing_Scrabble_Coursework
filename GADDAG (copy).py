# The GADDAG class relies on having a well defined node class
class Node:
	#nodeCount = 0			# I had this line and the first in __init__() so that I could see how many nodes are made with selected input for testing purposes
	def __init__(self, wordA):	# A node knows its arcs (which form the ends of the 'word'), its own letter, and if it is the end of a word.
		#Node.nodeCount += 1
		self.nodeLetter = wordA[0]		
		self.hasArcs = False
		self.arcLetters = {}	
		self.canTerminate = False		# canTerminate is True if this path forms a valid word
		self.addArc(wordA[1:])
	
	# basically checks if the word we've reached is a real word
	def getCanTerminate(self, canTerminate = None):
		return self.canTerminate	
		
	# gets all of the possible letters which can follow this one to potentially reach the end of another word
	def getArcLetters(self, arcDict = None):	
		return self.arcLetters	
	
	# same functionality as CanTerminate()
	def isWord(self, canTerminate = None):
		return self.canTerminate
	
	# returns the letter of this node
	def getNodeLetter(self, letter = None):
		return self.nodeLetter
		
	# adds an arc from the current node to the next node to form the word 'wordA', and recursively repeats for the next word until the end of the word has been reached
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
		self.startNode = Node("*")		# this is just treated as the starting point; the root node		
		for word in elements:			# adds each word into the structure
			self.addWord(word)			
			
	# allows for an easy way, without having to directly access objects of the node class from the outside, to get to a node defined by a certain word.
	def navigateToNode(self, wordA, currentNode = None):
		if currentNode == None:		# If no node was passed in for currentNode, this means that we are at the start of a word, and we look for edges connected to the root node
			currentNode = self.startNode		
		try:
			if len(wordA) > 0:
				return  self.navigateToNode(wordA[1:], currentNode.arcLetters[wordA[0]])
			else:
				return currentNode				# returns the node
		except:		# if no such node exists in the structure, this means that the word we searched for is not entered in the GADDAG structure, and is therefore definitely not a valid word
			return None			

	def findNodes(self, wordA, currentWord = "", currentNode = None):
		if currentNode == None:
			currentNode = self.startNode	
		nodesWordsCollection = []
		
		wordAtoB = wordA			
		for char in wordA:
			if char != "*":		# if it is a defined character...
				currentNode = self.navigateToNode(char, currentNode)
				currentWord += wordAtoB[0]
				wordAtoB = wordAtoB[1:]
			else:		# if the wildcarc '*' character is met, then we need to check for every possibility from the current node, as in scrabble terms, it means that this letter can become any letter, so with the AI we would look for the path which gives us the highest scoring word.
				for charOfNode in currentNode.getArcLetters():
					nodesWordsCollection += self.findNodes(charOfNode + wordAtoB[1:], currentWord, currentNode)
				break				
				
		if wordAtoB == "" and currentNode != None:	# if there were no wildcards, then we don't need to worry about geting multile results from this search
			return [[currentWord, currentNode]]
		else:		# however if there were wildcards, then there should be a two dimensional list, where the top list has more than one element
			return nodesWordsCollection
	
	"""
	def addWord(self, word):			# this is used when i need examples with a simple structure
		self.startNode.addArc(word)
	"""
	
	# To understand my method for addingwords, one must at least see the diagram of how a partly minimised GADDAG structure looks in my references, and think about how this achieves that. I will not go into detail to explain this, as there are full academic papers on how GADDAG works (which I have referenced)
	def addWord(self, word):
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









































