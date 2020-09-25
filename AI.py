import pygame
import Player
import Game	
import GADDAG

class AI(Player.Player):
	def __init__(self, nickname, game):
		global gaddag
		super(AI, self).__init__(nickname, game)
		#self.my_gaddag = gaddag
		self.board_rows = []
		self.board_columns = []
		#self.vertical_words = []
		#self.horizontal_words = []
		self.best_words = []
		self.alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

		
	def GetRowsAndColumns(self):
		self.board_rows = []
		self.board_columns = [""] * len(self.the_board[0])
		row_num = 0
		while row_num < len(self.the_board):
			column_num = 0
			row_string = ""
			while column_num < len(self.the_board[row_num]):
				char = self.GetLetterOfTileInHolderAtPos((column_num, row_num))
				if char == None:
					char = " "
				row_string += char
				self.board_columns[column_num] += char
				column_num += 1	
			self.board_rows.append(row_string)
			row_num += 1
			
	
		
	def FindBestWord(self):
		for y in range(15):
			for x in range(15):
				HookH(x, y)
				HookV(x, y)
		self.best_words.sort(key=operator.itemgetter(1), reverse = True)
		#self.rack = [("C", 4), ("R", 1), ("E", 1), ("T", 2)]	
		"""
		y = 0
		for y, row in enumerate(self.rack):
			for x, board_tile in enumerate(row):
				if board_tile[1] != None:
					pass
		"""
		return self.best_words[0]
		
	
	def VerticalWordAtPos(x, y):
		# checks if the tile which was placed down actually forms a word in the vertical direction
		pass
		
	def HookH(x, y, start_pos = None, forward = False, word = "", tile_placed = False):
		letter = self.in_game.GetLetterOfTileInHolderAtPos((x, y))
		if start_pos == None:
			start_pos = (x, y)
		
		if letter != None:
			word += letter
		
		score = self.in_game.CalculateWordScore()
		if tile_placed and gaddag.checkIsWord(word) and VerticalWordAtPos(x, y):
			self.best_words.append((word, score, start_pos, "H"))
			
		if x > 0 and not forward:
			x -= 1
		elif x == 0 and not forward:
			forward = True
			x = start_pos[0] + 1
			word += "@"
		elif x < 14 and forward:
			x += 1
		elif x >= 14 and forward:
			return
		elif x < 0:
			raise

		moved = False
		next_letter = self.in_game.GetLetterOfTileInHolderAtPos((x, y))
		if next_letter != None:
			self.HookH(x, y, start_pos, forward, word, tile_placed)
			moved = True
		else:
			for rack_pos in range(7):
				if self.rack[rack_pos] != None:
					if self.GetLetterTileAtPosition(rack_pos) == "*":
						for letter in self.alphabet:
							self.in_game.MoveRackTileToBoard(rack_pos, (x, y), letter)
							self.HookH(x, y, start_pos, forward, word, True)
							self.in_game.MoveBoardTileToRack((x, y), rack_pos)
					else:
						self.in_game.MoveRackTileToBoard(rack_pos, (x, y))
						self.HookH(x, y, start_pos, forward, word, True)
						self.in_game.MoveBoardTileToRack((x, y), rack_pos)					
		
		if not moved and not forward:
			forward = True
			self.HookH(start_pos[0] + 1, y, start_pos, forward, word + "@", True)
		
				
	def MakePlay(self):
		self.GetRowsAndColumns()
		self.findBestWord()
		self.in_game.PassTurn()
	
	
"""
test_board = [
			[["", None], ["", None], ["", None]],
			[["", None], ["TL", ("A", 1)], ["DW", None]],
			[["", None], ["", None], ["", None]]
			]
"""			
	