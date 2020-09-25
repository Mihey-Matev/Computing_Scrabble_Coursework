import pygame
import Player
import Game	
import GADDAG

class AI(Player.Player):
	def __init__(self, nickname, game, gaddag):
		self.gaddag = gaddag
		super(AI, self).__init__(nickname, game)
		#self.my_gaddag = gaddag
		self.board_rows = []
		self.board_columns = []
		#self.vertical_words = []
		#self.horizontal_words = []
		self.best_words = []
		self.alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
		#print("AI created")

	"""
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
	"""	
	
		
	def FindBestWord(self):
		if self.in_game.GetLetterOfTileInHolderAtPos((7, 7)) == None:
			for rack_pos in range(7):
				if self.GetLetterTileAtPosition(rack_pos) != None:
					if self.GetLetterTileAtPosition(rack_pos) != "*":
						self.in_game.MoveRackTileToBoard(rack_pos, (7, 7))
						self.HookH(x = 7, y = 7, poss_list = [(rack_pos, (7, 7))])
						self.HookV(x = 7, y = 7, poss_list = [(rack_pos, (7, 7))])	#x, y, start_pos = None, forward = False, word = "", tile_placed = False, poss_list = None
						self.in_game.MoveBoardTileToRack((7, 7), rack_pos)
					else:
						for letter in self.alphabet:
							self.in_game.MoveRackTileToBoard(rack_pos, (7, 7), letter)
							self.HookH(x = 7, y = 7, poss_list = [(rack_pos, (7, 7))])
							self.HookV(x = 7, y = 7, poss_list = [(rack_pos, (7, 7))])	#x, y, start_pos = None, forward = False, word = "", tile_placed = False, poss_list = None
							self.in_game.MoveBoardTileToRack((7, 7), rack_pos)					
		else:
			for y in range(15):
				for x in range(15):
					if self.in_game.GetLetterOfTileInHolderAtPos((x, y)) != None:
						if x == 14 or self.in_game.GetLetterOfTileInHolderAtPos((x + 1, y)) == None:
							self.HookH(x, y)
						if y == 14 or self.in_game.GetLetterOfTileInHolderAtPos((x, y + 1)) == None:
							self.HookV(x, y)
		#self.best_words.sort(key=operator.itemgetter(1), reverse = True)
		self.best_words.sort(key=lambda tup: tup[1], reverse = True)
		#self.rack = [("C", 4), ("R", 1), ("E", 1), ("T", 2)]	
		"""
		y = 0
		for y, row in enumerate(self.rack):
			for x, board_tile in enumerate(row):
				if board_tile[1] != None:
					pass
		"""
		if len(self.best_words) != 0:
			return self.best_words[0]
		
		
	def HorizontalWordAtPos(self, x, y):
		# checks if the tile which was placed down actually forms a word in the vertical direction
		start_pos = (x, y)
		working_pos = start_pos		
		forward = False		
		current_word = ""
		while self.in_game.GetLetterOfTileInHolderAtPos(working_pos) != None or not forward:
			current_word += self.in_game.GetLetterOfTileInHolderAtPos(working_pos)
			if not forward:
				working_pos = (working_pos[0] - 1, working_pos[1])
				if working_pos[0] < 0 or self.in_game.GetLetterOfTileInHolderAtPos(working_pos) == None:
					current_word += "@"
					forward = True
					working_pos = (start_pos[0] + 1, start_pos[1])
					if working_pos[0] > 14:
						break
			else:
				working_pos = (working_pos[0] + 1, working_pos[1])
				if working_pos[0] > 14:
						break
				
		if current_word[-1] == "@":
			current_word = current_word[:-1]
		if len(current_word) == 1:
			return True
		else:
			return self.gaddag.checkIsWord(current_word)
	
	
	def HookV(self, x, y, start_pos = None, forward = False, word = "", tile_placed = False, poss_list = None):
		if poss_list == None:
			poss_list = []		
		if start_pos == None:
			start_pos = (x, y)
			
		letter = self.in_game.GetLetterOfTileInHolderAtPos((x, y))
		if len(word) >= 1 and word[-1] != "@" and letter != None:
			word += letter
		elif len(word) == 0:
			word = letter
		
		#print (word)
		if tile_placed and self.gaddag.checkIsWord(word) and len(word) >= 0 and word[-1] != "@" and ((forward and y != 14 and self.in_game.GetLetterOfTileInHolderAtPos((x, y + 1)) == None) or (not forward and y != 0 and self.in_game.GetLetterOfTileInHolderAtPos((x, y - 1)) == None)):
			score = self.in_game.CalculateWordScore()
			#self.best_words.append((word, score, start_pos, "V"))
			self.best_words.append((tuple(poss_list), score))
			"""
			print ((tuple(poss_list), score))
			print (self.rack)
			print (x, y, word)
			"""
			
		if y > 0 and not forward:
			y -= 1
		elif y == 0 and not forward:
			forward = True
			y = start_pos[0] + 1
			word += "@"
		elif y < 14 and forward:
			y += 1
		elif y >= 14 and forward:
			return
		elif y < 0:
			raise

		moved = False
		next_letter = self.in_game.GetLetterOfTileInHolderAtPos((x, y))
		if next_letter != None:
			self.HookV(x, y, start_pos, forward, word, tile_placed, poss_list)
			moved = True
		else:
			for rack_pos in range(7):
				rack_letter = self.rack[rack_pos]
				if rack_letter != None:
					rack_letter = self.rack[rack_pos][0]
					if self.GetLetterTileAtPosition(rack_pos) == "*":
						for test_letter in self.alphabet:
							if self.gaddag.navigateToNode(word + test_letter) != None:
								self.in_game.MoveRackTileToBoard(rack_pos, (x, y), test_letter)
								if self.HorizontalWordAtPos(x, y):
									poss_list.append((rack_pos, (x, y), test_letter))
									self.HookV(x, y, start_pos, forward, word, True, poss_list)
									poss_list.pop(-1)
								self.in_game.MoveBoardTileToRack((x, y), rack_pos)
					else:
						if self.gaddag.navigateToNode(word + rack_letter) != None:
							self.in_game.MoveRackTileToBoard(rack_pos, (x, y))
							if self.HorizontalWordAtPos(x, y):
								poss_list.append((rack_pos, (x, y)))
								self.HookV(x, y, start_pos, forward, word, True, poss_list)
								poss_list.pop(-1)
							self.in_game.MoveBoardTileToRack((x, y), rack_pos)			
					moved = True
		#self.in_game.GetLetterOfTileInHolderAtPos((x, y))
		#if not moved and not forward:
		#	forward = True
		if not "@" in word and self.in_game.GetLetterOfTileInHolderAtPos((x, y - 1)) == None:
			self.HookV(x, start_pos[1], start_pos, True, word + "@", tile_placed, poss_list)
		#elif not moved and forward:
		if not moved and forward:
			return
		
	
	def VerticalWordAtPos(self, x, y):
		# checks if the tile which was placed down actually forms a word in the vertical direction
		start_pos = (x, y)
		working_pos = start_pos	
		#print ("in verticalwordatpos")
		#print(self.in_game.GetLetterOfTileInHolderAtPos(working_pos))
		forward = False		
		current_word = ""
		while self.in_game.GetLetterOfTileInHolderAtPos(working_pos) != None or not forward:
			#print ("in verticalwordatpos loop")
			#print (self.in_game.GetLetterOfTileInHolderAtPos(working_pos), forward)
			current_word += self.in_game.GetLetterOfTileInHolderAtPos(working_pos)
			if not forward:
				working_pos = (working_pos[0], working_pos[1] - 1)
				if working_pos[1] < 0 or self.in_game.GetLetterOfTileInHolderAtPos(working_pos) == None:
					#print ("hi")
					current_word += "@"
					forward = True
					working_pos = (start_pos[0], start_pos[1] + 1)
					if working_pos[1] > 14:
						break
			else:
				working_pos = (working_pos[0], working_pos[1] + 1)
				if working_pos[1] > 14:
					break
				
		if current_word[-1] == "@":
			current_word = current_word[:-1]
		if len(current_word) == 1:
			return True
		else:
			return self.gaddag.checkIsWord(current_word)
		
		
	def HookH(self, x, y, start_pos = None, forward = False, word = "", tile_placed = False, poss_list = None):
		if poss_list == None:
			poss_list = []		
		if start_pos == None:
			start_pos = (x, y)
			
		#print ("hi from HookH")
		#print (self)
		letter = self.in_game.GetLetterOfTileInHolderAtPos((x, y))
		if len(word) >= 1 and word[-1] != "@" and letter != None:
			word += letter
		elif len(word) == 0:
			word = letter
		
		"""
		print (tile_placed)
		print (word)
		print (self.gaddag.checkIsWord(word))
		if tile_placed:
			print (self.VerticalWordAtPos(x, y))
		print (forward)
		print (self.in_game.GetLetterOfTileInHolderAtPos((x + 1, y)))
		print (self.in_game.GetLetterOfTileInHolderAtPos((x - 1, y)))
		"""
		#print (word)
		if tile_placed and self.gaddag.checkIsWord(word) and len(word) >= 1 and word[-1] != "@" and ((forward and x != 14 and self.in_game.GetLetterOfTileInHolderAtPos((x + 1, y)) == None) or (not forward and x != 0 and self.in_game.GetLetterOfTileInHolderAtPos((x - 1, y)) == None)):
			#self.best_words.append((word, score, start_pos, "H"))
			score = self.in_game.CalculateWordScore()
			self.best_words.append((tuple(poss_list), score))
			"""
			print ((tuple(poss_list), score))
			print (self.rack)
			print (x, y, word)
			"""
			
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
		#print (next_letter)		
		if next_letter != None:
			self.HookH(x, y, start_pos, forward, word, tile_placed, poss_list)
			moved = True
		else:
			for rack_pos in range(7):
				rack_letter = self.rack[rack_pos]
				if rack_letter != None:
					rack_letter = self.rack[rack_pos][0]
					if self.GetLetterTileAtPosition(rack_pos) == "*":
						for test_letter in self.alphabet:
							if self.gaddag.navigateToNode(word + test_letter) != None:
								self.in_game.MoveRackTileToBoard(rack_pos, (x, y), test_letter)
								if self.VerticalWordAtPos(x, y):
									poss_list.append((rack_pos, (x, y), test_letter))
									self.HookH(x, y, start_pos, forward, word, True, poss_list)
									poss_list.pop(-1)
								self.in_game.MoveBoardTileToRack((x, y), rack_pos)
					else:
						#print (type(word))
						if self.gaddag.navigateToNode(word + rack_letter) != None:
							self.in_game.MoveRackTileToBoard(rack_pos, (x, y))
							if self.VerticalWordAtPos(x, y):
								poss_list.append((rack_pos, (x, y)))
								self.HookH(x, y, start_pos, forward, word, True, poss_list)
								poss_list.pop(-1)
							self.in_game.MoveBoardTileToRack((x, y), rack_pos)			
					moved = True
		#self.in_game.GetLetterOfTileInHolderAtPos((x, y))
		#if not moved and not forward:
		#	forward = True
		#print (start_pos)
		if not "@" in word and self.in_game.GetLetterOfTileInHolderAtPos((x - 1, y)) == None:
			self.HookH(start_pos[0], y, start_pos, True, word + "@", tile_placed, poss_list)
		#elif not moved and forward:
		if not moved and forward:
			return
		
	
	def PlaceLetters(self, pos_struct_tuple):
		#i = 0
		#original_pos = pos_struct_tuple[2]
		#working_pos = original_pos
		#forward = False
		#while i < len(pos_struct_tuple[0]):# - pos_struct_tuple[0].count("@"):
		for pos_pair in pos_struct_tuple[0]:
			print (pos_pair)
			if len(pos_pair) == 2:
				self.in_game.MoveRackTileToBoard(pos_pair[0], pos_pair[1])
			elif len(pos_pair) == 3:
				self.in_game.MoveRackTileToBoard(pos_pair[0], pos_pair[1], pos_pair[2])
			else:
				raise
			"""
			if forward and pos_struct_tuple[3] == "H":
				working_pos = (working_pos[0] + 1, working_pos[1])
			elif not forward and pos_struct_tuple[3] == "H":
				working_pos = (working_pos[0] - 1, working_pos[1])
			elif forward and pos_struct_tuple[3] == "V":
				working_pos = (working_pos[0], working_pos[1] + 1)
			elif not forward and pos_struct_tuple[3] == "V":
				working_pos = (working_pos[0], working_pos[1] - 1)
			"""
			#i += 1
			#self.in_game.MoveBoardTileToBoardPos()
	

	def MakePlay(self):
		#print ("---------------------------------------------------------------------------")
		#print (self.best_words)
		print ("---------------------------------------------------------------------------")
		for row in self.in_game.the_board:
			print([str(n[0]) + " " for n in row])
		print ("---------------------------------------------------------------------------")
		#for n in self.GetRowsAndColumns():
		#	print (n)
		#print (self.best_words)
		best_word = self.FindBestWord()
		print ("---------------------------------------------------------------------------")
		#print (self.best_words)
		print (best_word)
		if best_word != None:
			self.PlaceLetters(best_word)
			self.best_words.clear()
			self.in_game.SubmitWord()
		else:
			self.in_game.PassTurn()		
		print ("---------------------------------------------------------------------------")
		for row in self.in_game.the_board:
			print([str(n[0]) + " " for n in row])
			
		print ("\n\n\n")
	
	
"""
test_board = [
			[["", None], ["", None], ["", None]],
			[["", None], ["TL", ("A", 1)], ["DW", None]],
			[["", None], ["", None], ["", None]]
			]
"""			
	