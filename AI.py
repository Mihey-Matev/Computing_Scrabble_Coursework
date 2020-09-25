import pygame
import Player
import Game	
import GADDAG

class AI(Player.Player):
	def __init__(self, nickname, game, gaddag):
		self.my_gaddag = gaddag
		self.board_rows = []
		self.board_columns = []
		self.vertical_words = []
		self.horizontal_words = []

		
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
			
	
		
	def findBestWord(self):
		
		#self.rack = [("C", 4), ("R", 1), ("E", 1), ("T", 2)]	
		"""
		y = 0
		for y, row in enumerate(self.rack):
			for x, board_tile in enumerate(row):
				if board_tile[1] != None:
					pass
		"""
				
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
	