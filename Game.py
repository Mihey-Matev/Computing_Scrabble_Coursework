import random
import pygame
import sys
import random
import Player
import AI
import final_gaddag_v6

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
		dict_file = open(str(sys.path[0]) + "/dictionary", "r")
		self.my_dict = dict_file.read().strip().upper().split("\n")
		dict_file.close()
		#print(self.my_dict[:20])
		
		self.current_player_num = random.randint(0, len(self.players) - 1)
		self.current_player = self.players[self.current_player_num]
		self.BeforeEachTurn()
		
		# This is the main board behin the scenes. Each third level list of three elements contains the multiplier type (as a string), the tile which it holds (initially no tile, but as the players keep submitting words, that will change), and whether it has been locked (i.e. whether a tile has been placed there in a previous turn; this will be useful once calculating the score)
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
		
		# gameplay variables; work similarly to how they do in GameScene
		self.tile_placement_locations = []		# helps out in checking if the word submitted is valid and putting all tiles back onto the player's rack if they wish
		self.winner = None
		self.BeforeEachTurn()
		
	# Moves a tile from a given position in the player's rack to a given position on the board
	def MoveRackTileToBoard(self, from_pos, to_pos, wild_card_letter = None):	# a wild card lettertile is one which can be any letter; this is the reason for the last parameter
		if self.current_player.GetLetterTiles()[from_pos][1] != 0:		# We can check if the tile is a wildcard by checking its score; if it's zero, it's a wildcard.
			self.the_board[to_pos[1]][to_pos[0]][0] = self.current_player.GetLetterTiles()[from_pos]	# If not a wildcard, we can just move it.
		else:		# If it is a wildcard, then we need to also change its letter as we move it to whatever was passed in as wild_card_letter
			self.the_board[to_pos[1]][to_pos[0]][0] = (wild_card_letter, 0)
		self.current_player.SetRackLetterTile(from_pos, None)	# We make sure to remove the tile which was moved from the player's rack, so we don't have any extra copies of tiles
		self.tile_placement_locations.append(to_pos)	
	
	# This allows the player to move their tiles around their rack
	def MoveRackTileToRackPos(self, from_pos, to_pos):
		self.current_player.SetRackLetterTile(to_pos, self.current_player.GetLetterTiles()[from_pos])
		self.current_player.SetRackLetterTile(from_pos, None)
	
	# Allows the player to move a tile around on the board (instead of having to put it back on their rack first)
	# for explanation on how the wildcard is dealt with, see above; the only difference is that this time we are just inspetcing the tile on the board instead of the tile in the player's rack
	def MoveBoardTileToBoardPos(self, from_pos, to_pos, wild_card_letter = None):	# a wild card lettertile is one which can be any letter; this is the reason for the last parameter
		self.tile_placement_locations[self.tile_placement_locations.index(from_pos)] = to_pos
		if self.the_board[from_pos[1]][from_pos[0]][0][1] != 0:
			self.the_board[to_pos[1]][to_pos[0]][0] = self.the_board[from_pos[1]][from_pos[0]][0]
		else:
			self.the_board[to_pos[1]][to_pos[0]][0] = (wild_card_letter, 0)
		self.the_board[from_pos[1]][from_pos[0]][0] = None
	
	# allows the player to move a tile from the board back onto their rack	
	def MoveBoardTileToRack(self, from_pos, to_pos):
		if self.the_board[from_pos[1]][from_pos[0]][0][1] != 0:		# Similar checking for wildcard as above
			self.current_player.SetRackLetterTile(to_pos, self.the_board[from_pos[1]][from_pos[0]][0])
		else:
			self.current_player.SetRackLetterTile(to_pos, ("*", 0))		# if the tile which was on the board was a wildcard, then it is returned to their rack as if it was not affected by the letter cahnge
		self.tile_placement_locations.pop(self.tile_placement_locations.index(from_pos))
		self.the_board[from_pos[1]][from_pos[0]][0] = None			
		
	# checks if the word which has just been submitted on the board is valid
	def IsWordValid(self):
		# Firstly we check if the locations of the tiles which the player palces down are all in the same row or same column; if they aren't, then the word submitted is invalid
		valid = False
		if len(self.tile_placement_locations) >= 2:			
			columnar_word = False
			# check if the rows are the same by comparing each x coordinate of the tiles to each other
			n = 0
			while n < len(self.tile_placement_locations) - 1 and not columnar_word:
				pos1 = self.tile_placement_locations[n]
				for pos2 in self.tile_placement_locations[n+1:]:
					if pos1[0] != pos2[0]:
						columnar_word = True
						break
				n += 1
			if not columnar_word:
				valid = True
			
			# check if the columns are the same by comparing each y coordinate of the tiles to each other
			n = 0
			while n < len(self.tile_placement_locations) - 1 and columnar_word:
				pos1 = self.tile_placement_locations[n]
				for pos2 in self.tile_placement_locations[n+1:]:
					if pos1[1] != pos2[1]:
						columnar_word = False
						break
				n += 1
			if columnar_word:
				valid = True
		elif len(self.tile_placement_locations) == 1:
			valid = True
		else:
			valid = False			
		# then we can check if the word is connected to a branch of the already existing words
		if valid:
			for pos in self.tile_placement_locations:	# check each tile which has been placed down for whether its position is valid; if one is invalid, then the word cannot be submitted.
				if not self.IsTileConnectedToSubmittedTiles(pos):
					valid = False
					break							
		if valid:
			valid = self.IsWordAWord()			
		return valid		
	
	def IsWordAWord(self):
		row_strings = []
		column_strings = [""] * len(self.the_board[0])
		row_num = 0
		column_string = ""
		while row_num < len(self.the_board):
			column_num = 0
			row_string = ""
			while column_num < len(self.the_board[row_num]):
				char = self.GetLetterOfTileInHolderAtPos((column_num, row_num))
				if char != None:
					row_string += self.GetLetterOfTileInHolderAtPos((column_num, row_num))
					if char == None:
						char = " "
					column_strings[column_num] += char
				elif row_string != "":
					row_strings.append(row_string)
					row_string = ""
				column_num += 1		
			if row_string != "":
				row_strings.append(row_string)
			row_num += 1
			
		i = 0
		while i < len(column_strings):
			if column_strings[i] == "":
				column_strings.pop(i)
			elif " " in column_strings[i]:
				column_strings += column_strings.pop(i).split(" ")
			else:
				i += 1
		"""
		print ("-------------------------------")
		print (row_strings)
		print (column_strings)
		print ("-------------------------------")
		"""
		valid = True
		for string in row_strings:
			if not string in self.my_dict:
				valid = False
				break
		#print (valid)
		if valid:
			for string in column_strings:
				if not string in self.my_dict:
					valid = False
					break
		#print (valid)
		
		if len(row_strings) == 1 and len(column_strings) == 1 and row_strings[0] in self.my_dict:
			valid = True
					
		return valid
		
		
	# this function returns true if the tile being tested is in some way connected to previously submitted tiles; otherwise, it returns false. If the tile is not in the self.tile_placement_locations list, then it is assumed that the tile being tested is a submitted tile, which is the base case.
	def IsTileConnectedToSubmittedTiles(self, tile_relative_pos, previous_pos = None):	# the last parameter is to make sure that two tiles don't infinetly check if each other are in a valid position
		valid = False
		if tile_relative_pos == (7, 7) and tile_relative_pos in self.tile_placement_locations:	# if this is the first word being put down, then allow user to place it down on the centre piece without any problems
			valid = True
		elif tile_relative_pos in self.tile_placement_locations:	# if the tile placed down 
			for pos in [(tile_relative_pos[0] + 1, tile_relative_pos[1]), (tile_relative_pos[0] - 1, tile_relative_pos[1]), (tile_relative_pos[0], tile_relative_pos[1] + 1), (tile_relative_pos[0], tile_relative_pos[1] - 1)]:
				if pos != previous_pos and (self.IsTileConnectedToSubmittedTiles(pos, tile_relative_pos)):
					valid = True
		elif tile_relative_pos[1] >= 0 and tile_relative_pos[1] <= 14 and tile_relative_pos[0] >= 0 and tile_relative_pos[0] <= 14 and self.the_board[tile_relative_pos[1]][tile_relative_pos[0]][2] == True:
			valid = True
		return valid
	
	# calculates the number of points which the submitted word should score
	def CalculateWordScore(self):
		return 0	
	
	# swaps the turns of players
	def NextPlayer(self):
		self.current_player_num = (self.current_player_num + 1) % len(self.players)
		self.current_player = self.players[self.current_player_num]	
		
	# this is the method called once the user presses the 'submit word' button in GameScene (i.e. once they want to confirm their play)
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

	# This method gives the players lettertiles
	def DealOutLetterTiles(self, player = None):
		if player == None:
			player = self.current_player
		
		num_of_letters_to_give = player.GetLetterTiles().count(None)
		letters_to_give_player = []
		
		# Choosing a random tile by counting how many tiles are left in the bag, taking a random integer between this value and 1, and looking for which group of tiles this number represents; this is done for each tile which is None in the player's rack
		i = 0
		while i < num_of_letters_to_give and sum(self.the_tile_bag.values()) > 0:						
			rand_tile_num = random.randint(1, sum(self.the_tile_bag.values()))
			for tile, num in self.the_tile_bag.items():
				if num >= rand_tile_num:
					self.the_tile_bag[tile] -= 1
					letters_to_give_player.append(tile)
					break
				else:
					rand_tile_num -= num
			i += 1
		player.PopulateRack(letters_to_give_player)		
	
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
	
	# gets the tiles which is at a certain position on the board
	def GetTileAtPos(self, x, y):
		return self.the_board[y][x][0]	
	
	def GetNextPlayer(self):
		return self.players[(self.current_player_num + 1) % len(self.players)]		
	
	def GetNextPlayerName(self):
		return self.GetNextPlayer().GetName()	
	
	def GetNextPlayerScore(self):
		return self.GetNextPlayer().GetScore()	
		
	# and intermediate method which is called before each turn
	def BeforeEachTurn(self):
		self.DealOutLetterTiles()	
		
	def GetLetterOfTileInHolderAtPos(self, pos):
		if self.the_board[pos[1]][pos[0]][0] != None:
			return self.GetTileAtPos(pos[0], pos[1])[0]
			#return self.the_board[pos[1]][pos[0]][0][0]
	
	def GetScoreOfTileInHolderAtPos(self, pos):
		if self.the_board[pos[1]][pos[0]][0] != None:
			return self.GetTileAtPos(pos[0], pos[1])[1]
			#return self.the_board[pos[1]][pos[0]][0][1]
		
	# gets the remaining lettertiles which the current player is meant to be able to see; this is used when the player wants to see the tiles left in the tilebag (i.e. when they press the 'Tile Bag' button)
	def GetRemainingTilesForCurrentPlayer(self):
		return_dict = dict(self.the_tile_bag)
		for n in self.GetNextPlayer().GetLetterTiles():
			if n != None:
				return_dict[n] += 1
		
		for key in dict(return_dict):
			return_dict[key[0]] = return_dict.pop(key)
		return return_dict	
	
	# If the player chooses to swap their tiles out, this is the method that deals with it. It takes in the position on the rack of the tiles which the player wants to swap, then deals them out new tiles.
	def SwapTiles(self, positions_of_rack_to_swap):
		old_tiles = []
		for n, tile in enumerate(self.current_player.GetLetterTiles()):
			if n in positions_of_rack_to_swap:
				old_tiles.append(tile)
				self.current_player.SetRackLetterTile(n, None)
		
		self.DealOutLetterTiles(self.current_player)
		for tile in old_tiles:
			self.the_tile_bag[tile] += 1

	
	
	
	
	