import pygame
import random
import Player
#import TileBag
import AI

class Game:
	def __init__(self, player_names, AI_names):
		self.players = [Player.Player(x) for x in player_names] + [AI.AI(x) for x in AI_names]
		self.the_tile_bag = {
							("A", 1): 9,
							("B", 4): 2,
							("C", 4): 2,
							("D", 2): 5,
							("E", 1): 13,
							("F", 4): 2,
							("G", 3): 3,
							("H", 3): 4,
							("I", 1): 8,
							("J", 10): 1,
							("K", 5): 1,
							("L", 2): 4,
							("M", 4): 2,
							("N", 2): 5,
							("O", 1): 8,
							("P", 4): 2,
							("Q", 10): 1,
							("R", 1): 6,
							("S", 1): 5,
							("T", 1): 7,
							("U", 2): 4,
							("V", 5): 2,
							("W", 4): 2,
							("X", 8): 1,					
							("Y", 3): 2,
							("Z", 10): 1,
							("*", 0): 2
							}
		
		self.current_player_num = random.randint(0, len(self.players) - 1)
		
		# This is the main board behin the scenes. Each third level list of two elements contains the multiplier type (as a string) and the tile which it holds (initially no tile, but as the players keep submitting words, that will change)
		self.the_submitted_l_board = [
									[["", None], ["", None], ["", None], ["TW", None], ["", None], ["", None], ["TL", None], ["", None], ["TL", None], ["", None], ["", None], ["TW", None], ["", None], ["", None], ["", None]],
									[["", None], ["", None], ["DL", None], ["", None], ["", None], ["DW", None], ["", None], ["", None], ["", None], ["", None], ["", None], ["DL", None], ["", None], ["", None], ["", None]],
									[["", None], ["DL", None], ["", None], ["", None], ["DL", None], ["", None], ["", None], ["", None], ["", None], ["", None], ["DL", None], ["", None], ["", None], ["DL", None], ["", None]],
									[["TW", None], ["", None], ["", None], ["TL", None], ["", None], ["", None], ["", None], ["DW", None], ["", None], ["", None], ["", None], ["TL", None], ["", None], ["", None], ["TW", None]],
									[["", None], ["", None], ["DL", None], ["", None], ["", None], ["", None], ["DL", None], ["", None], ["DL", None], ["", None], ["", None], ["", None], ["DL", None], ["", None], ["", None]],
									[["", None], ["DW", None], ["", None], ["", None], ["", None], ["TL", None], ["", None], ["", None], ["", None], ["TL", None], ["", None], ["", None], ["", None], ["DW", None], ["", None]],
									[["TL", None], ["", None], ["", None], ["", None], ["DL", None], ["", None], ["", None], ["", None], ["", None], ["", None], ["DL", None], ["", None], ["", None], ["", None], ["TL", None]],
									[["", None], ["", None], ["", None], ["DW", None], ["", None], ["", None], ["", None], ["+", None], ["", None], ["", None], ["", None], ["DW", None], ["", None], ["", None], ["", None]],
									[["TL", None], ["", None], ["", None], ["", None], ["DL", None], ["", None], ["", None], ["", None], ["", None], ["", None], ["DL", None], ["", None], ["", None], ["", None], ["TL", None]],
									[["", None], ["DW", None], ["", None], ["", None], ["", None], ["TL", None], ["", None], ["", None], ["", None], ["TL", None], ["", None], ["", None], ["", None], ["DW", None], ["", None]],
									[["", None], ["", None], ["DL", None], ["", None], ["", None], ["", None], ["DL", None], ["", None], ["DL", None], ["", None], ["", None], ["", None], ["DL", None], ["", None], ["", None]],
									[["TW", None], ["", None], ["", None], ["TL", None], ["", None], ["", None], ["", None], ["DW", None], ["", None], ["", None], ["", None], ["TL", None], ["", None], ["", None], ["TW", None]],
									[["", None], ["DL", None], ["", None], ["", None], ["DL", None], ["", None], ["", None], ["", None], ["", None], ["", None], ["DL", None], ["", None], ["", None], ["DL", None], ["", None]],
									[["", None], ["", None], ["DL", None], ["", None], ["", None], ["DW", None], ["", None], ["", None], ["", None], ["", None], ["", None], ["DL", None], ["", None], ["", None], ["", None]],
									[["", None], ["", None], ["", None], ["TW", None], ["", None], ["", None], ["TL", None], ["", None], ["TL", None], ["", None], ["", None], ["TW", None], ["", None], ["", None], ["", None]]
									]
		
		# Creates an independent copy of the board; this will be what is gonig to be displayed. If it is a valid board after being submitted, self.the_submitted_l_board will also take on its value
		self.display_board = [[self.the_submitted_l_board[y][x][:] for y in range(len(self.the_submitted_l_board))] for x in range(len(self.the_submitted_l_board[0]))]
		
		
	def GetCurrentPlayerName(self):
		return self.current_player.GetName()
	
	
	def GetDisplayBoard(self):
		return self.display_board
	
	
	def GetNextPlayerName(self):
		return self.players[(self.current_player_num + 1) % len(self.players)].GetName()
	
	
	def GetNextPlayerScore(self):
		return self.players[(self.current_player_num + 1) % len(self.players)].GetScore()
	
	
	def GetCurrentPlayerLetterTiles(self):
		return self.current_player.GetLetterTiles()
	
	
	def GetCurrentPlayerScore(self):
		return self.current_player.GetScore()
		
	
	def SubmitWord(self):
		self.current_player = self.players[(self.current_player_num + 1) % len(self.players)]
		
		
	# gets the remaining lettertiles which the current player is meant to be able to see
	def GetRemainingTilesForCurrentPlayer(self):
		return [kept_tile for kept_tile in [y for x in [self.the_tile_bag[tile] * tile for tile in self.the_tile_bag] for y in x] if kept_tile not in self.GetCurrentPlayerLetterTiles()]
	
	
	
	
	
	
	