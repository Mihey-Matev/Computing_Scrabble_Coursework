import pygame
import Player
import Game	
import final_gaddag_v6

class AI(Player.Player):
	def __init__(self, nickname):
		super().__init__(nickname)
		my_gaddag = final_gaddag_v6.Gaddag(["AND", "THE", "RAT", "CAN", "EAT", "MAN", "SET", "MET", "BET", "CAT", "CAR", "CATS"])
		
		
	def findBestWord(self, board):
		self.rack = [("C", 4), ("R", 1), ("E", 1), ("T", 2)]
		
		y = 0
		for y, row in enumerate(self.rack):
			for x, board_tile in enumerate(row):
				if board_tile[1] != None:
					pass
	
	

test_board = [
			[["", None], ["", None], ["", None]],
			[["", None], ["TL", ("A", 1)], ["DW", None]],
			[["", None], ["", None], ["", None]]
			]
			
	