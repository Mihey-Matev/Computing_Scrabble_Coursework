import random
import pygame
		
class Player:
	def __init__(self, nickname, game):
		
		self.nickname = nickname
		self.SetScore(0)
		self.in_game = game
		
		# list of tuples containing a tile, where a tile is the tuple, containing the letter it represents as one element, and its point worth as another element
		# the 'dealing out' of letter tiles (i.e. population of the rack) will be done by the TileBag object in Game
		self.rack = [None] * 7
	
	def SetScore(self, newScore):
		self.score = newScore
		
	def GetScore(self):
		return self.score
	
	def PopulateRack(self, letters):
		m = 0
		for n in range(len(self.rack)):
			if self.rack[n] == None and m < len(letters):
				self.rack[n] = letters[m]
				m += 1	
	
	# shuffles the elements in the player's rack; this can then be displayed by GameScene (through Game)
	def ShuffleRack(self):
		random.shuffle(self.rack)		
		
	def UpdateScore(self, up_val):
		self.SetScore(self.GetScore() + up_val)		
		
	# gets the elements that the player's rack contains
	def GetLetterTiles(self):
		return self.rack	
	
	# changes one of the player's tiles in their rack to something new
	def SetRackLetterTile(self, pos, tile):
		self.rack[pos] = tile	
	
	def GetName(self):
		return self.nickname
	
	# Gets the tile which is at that position in their rack
	def GetLetterTileAtPosition(self, position):
		return self.rack[position]	
	
	
	"""Should probably move the tile movement methods from game to player"""
	# returns true if the placing was successful
	#def PlacePiece(lettertile_rack_pos, board_pos):
	#	return self.in_game.PlaceLetterTile(self.the_rack[lettertile_rack_pos], board_pos)