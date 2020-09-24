class Rack:
	def __init__(self):		
		print ("Not finished!")
		
class Player:
	def __init__(self):
		self.SetScore(0)
		self.rack = Rack()
	
	def SetScore(self, newScore):
		self.score = newScore
		
	def GetScore(self):
		return self.score
		
	def UpdateScore(self, upVal):
		SetScore(GetScore() + upVal)
		

class AI(Player):
	def __init__(self):
		super().__init__()
	