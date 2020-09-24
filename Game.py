import random
import pygame
import random
import Player
#import LLetterTile
#import TileBag
import AI

class Game:
	def __init__(self, player_names, AI_names):
		self.players = [Player.Player(x, self) for x in player_names] + [AI.AI(x) for x in AI_names]
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
		self.current_player = self.players[self.current_player_num]
		self.BeforeEachTurn()
		
		# This is the main board behin the scenes. Each third level list of three elements contains the multiplier type (as a string), the tile which it holds (initially no tile, but as the players keep submitting words, that will change), and whether it has been locked (i.e. whether a tile has been placed there in a previous turn; this will be useful once calculating the score)
		#self.the_submitted_board = 
		self.the_board = 			[
									[[None, "", False], [None, "", False], [None, "", False], [None, "TW", False], [None, "", False], [None, "", False], [None, "TL", False], [None, "", False], [None, "TL", False], [None, "", False], [None, "", False], [None, "TW", False], [None, "", False], [None, "", False], [None, "", False]],
									[[None, "", False], [None, "", False], [None, "DL", False], [None, "", False], [None, "", False], [None, "DW", False], [None, "", False], [None, "", False], [None, "", False], [None, "", False], [None, "", False], [None, "DL", False], [None, "", False], [None, "", False], [None, "", False]],
									[[None, "", False], [None, "DL", False], [None, "", False], [None, "", False], [None, "DL", False], [None, "", False], [None, "", False], [None, "", False], [None, "", False], [None, "", False], [None, "DL", False], [None, "", False], [None, "", False], [None, "DL", False], [None, "", False]],
									[[None, "TW", False], [None, "", False], [None, "", False], [None, "TL", False], [None, "", False], [None, "", False], [None, "", False], [None, "DW", False], [None, "", False], [None, "", False], [None, "", False], [None, "TL", False], [None, "", False], [None, "", False], [None, "TW", False]],
									[[None, "", False], [None, "", False], [None, "DL", False], [None, "", False], [None, "", False], [None, "", False], [None, "DL", False], [None, "", False], [None, "DL", False], [None, "", False], [None, "", False], [None, "", False], [None, "DL", False], [None, "", False], [None, "", False]],
									[[None, "", False], [None, "DW", False], [None, "", False], [None, "", False], [None, "", False], [None, "TL", False], [None, "", False], [None, "", False], [None, "", False], [None, "TL", False], [None, "", False], [None, "", False], [None, "", False], [None, "DW", False], [None, "", False]],
									[[None, "TL", False], [None, "", False], [None, "", False], [None, "", False], [None, "DL", False], [None, "", False], [None, "", False], [None, "", False], [None, "", False], [None, "", False], [None, "DL", False], [None, "", False], [None, "", False], [None, "", False], [None, "TL", False]],
									[[None, "", False], [None, "", False], [None, "", False], [None, "DW", False], [None, "", False], [None, "", False], [None, "", False], [None, "+", False], [None, "", False], [None, "", False], [None, "", False], [None, "DW", False], [None, "", False], [None, "", False], [None, "", False]],
									[[None, "TL", False], [None, "", False], [None, "", False], [None, "", False], [None, "DL", False], [None, "", False], [None, "", False], [None, "", False], [None, "", False], [None, "", False], [None, "DL", False], [None, "", False], [None, "", False], [None, "", False], [None, "TL", False]],
									[[None, "", False], [None, "DW", False], [None, "", False], [None, "", False], [None, "", False], [None, "TL", False], [None, "", False], [None, "", False], [None, "", False], [None, "TL", False], [None, "", False], [None, "", False], [None, "", False], [None, "DW", False], [None, "", False]],
									[[None, "", False], [None, "", False], [None, "DL", False], [None, "", False], [None, "", False], [None, "", False], [None, "DL", False], [None, "", False], [None, "DL", False], [None, "", False], [None, "", False], [None, "", False], [None, "DL", False], [None, "", False], [None, "", False]],
									[[None, "TW", False], [None, "", False], [None, "", False], [None, "TL", False], [None, "", False], [None, "", False], [None, "", False], [None, "DW", False], [None, "", False], [None, "", False], [None, "", False], [None, "TL", False], [None, "", False], [None, "", False], [None, "TW", False]],
									[[None, "", False], [None, "DL", False], [None, "", False], [None, "", False], [None, "DL", False], [None, "", False], [None, "", False], [None, "", False], [None, "", False], [None, "", False], [None, "DL", False], [None, "", False], [None, "", False], [None, "DL", False], [None, "", False]],
									[[None, "", False], [None, "", False], [None, "DL", False], [None, "", False], [None, "", False], [None, "DW", False], [None, "", False], [None, "", False], [None, "", False], [None, "", False], [None, "", False], [None, "DL", False], [None, "", False], [None, "", False], [None, "", False]],
									[[None, "", False], [None, "", False], [None, "", False], [None, "TW", False], [None, "", False], [None, "", False], [None, "TL", False], [None, "", False], [None, "TL", False], [None, "", False], [None, "", False], [None, "TW", False], [None, "", False], [None, "", False], [None, "", False]]
									]
		
		# Creates an independent copy of the board; this will be what is gonig to be displayed. If it is a valid board after being submitted, self.the_submitted_board will also take on its value
		#self.display_board = [[self.the_submitted_board[y][x][:] for y in range(len(self.the_submitted_board))] for x in range(len(self.the_submitted_board[0]))]
		
		# gameplay variables
		#self.selected_tile = None
		self.tile_placement_locations = []
		#self.rack_selection = None
		#self.board_selection = None
		self.winner = None
		self.BeforeEachTurn()

		
	def MoveRackTileToBoard(self, from_pos, to_pos, wild_card_letter = None):	# a wild card lettertile is one which can be any letter; this is the reason for the last parameter
		if self.current_player.GetLetterTiles()[from_pos][1] != 0:
			self.the_board[to_pos[1]][to_pos[0]][0] = self.current_player.GetLetterTiles()[from_pos]
		else:
			self.the_board[to_pos[1]][to_pos[0]][0] = (wild_card_letter, 0)
		self.current_player.SetRackLetterTile(from_pos, None)
		self.tile_placement_locations.append(to_pos)
		#print (self.current_player.rack)
	
	
	def MoveRackTileToRackPos(self, from_pos, to_pos):
		self.current_player.SetRackLetterTile(to_pos, self.current_player.GetLetterTiles()[from_pos])
		self.current_player.SetRackLetterTile(from_pos, None)
		#print (self.current_player.rack)

	
	def MoveBoardTileToBoardPos(self, from_pos, to_pos, wild_card_letter = None):	# a wild card lettertile is one which can be any letter; this is the reason for the last parameter
		self.tile_placement_locations[self.tile_placement_locations.index(from_pos)] = to_pos
		if self.the_board[from_pos[1]][from_pos[0]][0][1] != 0:
			self.the_board[to_pos[1]][to_pos[0]][0] = self.the_board[from_pos[1]][from_pos[0]][0]
		else:
			self.the_board[to_pos[1]][to_pos[0]][0] = (wild_card_letter, 0)
		self.the_board[from_pos[1]][from_pos[0]][0] = None	
		#print (self.current_player.rack)
	
	
	def MoveBoardTileToRack(self, from_pos, to_pos):
		if self.the_board[from_pos[1]][from_pos[0]][0][1] != 0:
			self.current_player.SetRackLetterTile(to_pos, self.the_board[from_pos[1]][from_pos[0]][0])
		else:
			self.current_player.SetRackLetterTile(to_pos, ("*", 0))
		self.tile_placement_locations.pop(self.tile_placement_locations.index(from_pos))
		self.the_board[from_pos[1]][from_pos[0]][0] = None		
		#print (self.current_player.rack)
	
		
	def IsWordValid(self):
		return True
	
	
	def CalculateWordScore(self):
		return 0
	
	
	def NextPlayer(self):
		self.current_player_num = (self.current_player_num + 1) % len(self.players)
		self.current_player = self.players[self.current_player_num]
	
		
	def SubmitWord(self):		
		if self.IsWordValid():
			self.current_player.UpdateScore(self.CalculateWordScore())
			for location in self.tile_placement_locations:
				self.the_board[location[1]][location[0]][2] = True
			self.tile_placement_locations.clear()
			self.NextPlayer()
			self.BeforeEachTurn()
			return True
		else:
			return False
		
	"""
	def CancelMoves(self):
		self.board_selection = None
		self.rack_selection = None
		self.the_game.CancelTileSelection()
	"""

	def DealOutLetterTiles(self, player = None):
		if player == None:
			player = self.current_player
		
		num_of_letters_to_give = player.GetLetterTiles().count(None)
		letters_to_give_player = []
		
		# Choosing a random tile by counting how many tiles are left in the bag, taking a random integer between this value and 1, and looking for which group of tiles this number represents; this is done for each tile which is None in the player's rack
		i = 0
		while i < num_of_letters_to_give and sum(self.the_tile_bag.values()) > 0:						
			rand_tile_num = random.randint(1, sum(self.the_tile_bag.values()))
			#print (sum(self.the_tile_bag.values()))
			for tile, num in self.the_tile_bag.items():
				if num >= rand_tile_num:
					#print (tile)
					self.the_tile_bag[tile] -= 1
					letters_to_give_player.append(tile)
					break
				else:
					rand_tile_num -= num
			i += 1
			
		#print (letters_to_give_player)
		#if len(letters_to_give_player) > 0:
		#	letters_to_give_player[-1] = ("*", 0)
		player.PopulateRack(letters_to_give_player)
		
	
	def SelectTileNum(self, tile_num):
		pass
	
	
	def GetWinner(self):
		return self.winner
	
	
	def Resign(self):
		self.winner = self.GetNextPlayerName()
		return self.GetWinner()
	
	
	def PassTurn(self):
		self.ReturnMovedTilesToRack()
		self.NextPlayer()
		self.BeforeEachTurn()
		
	
	def ShuffleTiles(self):		
		#self.ReturnMovedTilesToRack()
		self.current_player.ShuffleRack()
		
		
	def ReturnMovedTilesToRack(self):
		for rack_pos, tile in enumerate(self.current_player.GetLetterTiles()):
			if tile == None:
				self.MoveBoardTileToRack(self.tile_placement_locations[0], rack_pos)
	
	
	def GetCurrentPlayerLetterTiles(self):
		return self.current_player.GetLetterTiles()
	
			
	def GetCurrentPlayerName(self):
		return self.current_player.GetName()
	
	
	def GetCurrentPlayerScore(self):
		return self.current_player.GetScore()
		

	#def GetDisplayBoard(self):
	#	return self.the_board
	
	
	def GetTileAtPos(self, x, y):
		return self.the_board[y][x][0]
	
	
	def GetNextPlayer(self):
		return self.players[(self.current_player_num + 1) % len(self.players)]
		
	
	def GetNextPlayerName(self):
		return self.GetNextPlayer().GetName()
	
	
	def GetNextPlayerScore(self):
		return self.GetNextPlayer().GetScore()
	
		
	def BeforeEachTurn(self):
		self.DealOutLetterTiles()
		
		
	# gets the remaining lettertiles which the current player is meant to be able to see
	def GetRemainingTilesForCurrentPlayer(self):
		return_dict = dict(self.the_tile_bag)
		for n in self.GetNextPlayer().GetLetterTiles():
			if n != None:
				return_dict[n] += 1
		
		for key in dict(return_dict):
			return_dict[key[0]] = return_dict.pop(key)
		#print (return_dict)
		return return_dict
		#return [kept_tile for kept_tile in [y for x in [self.the_tile_bag[tile] * tile for tile in self.the_tile_bag] for y in x] if kept_tile not in self.GetCurrentPlayerLetterTiles()]
	
	
	def SwapTiles(self, positions_of_rack_to_swap):
		#print (positions_of_rack_to_swap)
		#old_tiles = [val for n, val in enumerate(self.current_player.GetLetterTiles()) if n in positions_of_rack_to_swap]
		old_tiles = []
		for n, tile in enumerate(self.current_player.GetLetterTiles()):
			if n in positions_of_rack_to_swap:
				old_tiles.append(tile)
				self.current_player.SetRackLetterTile(n, None)
		
		self.DealOutLetterTiles(self.current_player)
		for tile in old_tiles:
			self.the_tile_bag[tile] += 1
		#self.PassTurn()
	
	
	# returns true if the placing was successful
	#def PlaceLetterTile(lettertile, pos):
	#	if self.the_board[pos[1]][pos[0]][1] == None:
	#		self.the_board[pos[1]][pos[0]][1] = lettertile
	#		return True
	
	
	
	
	