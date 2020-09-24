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
			if self.rack[n] == None:
				self.rack[n] = letters[m]
				m += 1
	
	
	def ShuffleRack(self):
		random.shuffle(self.rack)
		
		
	def UpdateScore(self, up_val):
		self.SetScore(self.GetScore() + up_val)
		
		
	def GetLetterTiles(self):
		return self.rack
	
	
	def SetRackLetterTile(self, pos, tile):
		self.rack[pos] = tile
	
	
	def GetName(self):
		return self.nickname

	
	def GetLetterTileAtPosition(self, position):
		return self.rack[position]
	
	
	# returns true if the placing was successful
	def PlacePiece(lettertile_rack_pos, board_pos):
		return self.in_game.PlaceLetterTile(self.the_rack[lettertile_rack_pos], board_pos)