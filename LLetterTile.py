import pygame

class LLetterTile:
	def __init__(self, letter, point_worth):
		self.letter = letter
		self.point_worth = point_worth
	#	self.submitted = False
		
	#def SetSubmitted(self, submitted = True):
	#	self.submitted = submitted
		
	def GetLetter(self):
		return self.letter
	
	def GetPointWorth(self):
		return self.point_worth