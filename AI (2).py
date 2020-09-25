import pygame
import Player
import Game	
import GADDAG

class AI(Player.Player):
	def __init__(self, nickname, game, gaddag):
		self.gaddag = gaddag
		super(AI, self).__init__(nickname, game)
		self.board_rows = []
		self.board_columns = []
		self.best_words = []
		self.alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
	
		
	def FindBestWord(self):
		if self.in_game.GetLetterOfTileInHolderAtPos((7, 7)) == None:
			for rack_pos in range(7):
				rack_tile = self.GetLetterTileAtPosition(rack_pos)
				if rack_tile != None:
					if rack_tile[0] != "*":
						self.in_game.MoveRackTileToBoard(rack_pos, (7, 7))
						self.HookH(x = 7, y = 7, poss_list = [(rack_pos, (7, 7))], tile_placed = True)
						self.HookV(x = 7, y = 7, poss_list = [(rack_pos, (7, 7))], tile_placed = True)
						self.in_game.MoveBoardTileToRack((7, 7), rack_pos)
					else:
						for letter in self.alphabet:
							self.in_game.MoveRackTileToBoard(rack_pos, (7, 7), letter)
							self.HookH(x = 7, y = 7, poss_list = [(rack_pos, (7, 7), letter)], tile_placed = True)
							self.HookV(x = 7, y = 7, poss_list = [(rack_pos, (7, 7), letter)], tile_placed = True)
							self.in_game.MoveBoardTileToRack((7, 7), rack_pos)					
		else:
			for y in range(15):
				for x in range(15):
					if self.in_game.GetLetterOfTileInHolderAtPos((x, y)) != None:
						if x == 14 or self.in_game.GetLetterOfTileInHolderAtPos((x + 1, y)) == None:
							self.HookH(x, y)
						if y == 14 or self.in_game.GetLetterOfTileInHolderAtPos((x, y + 1)) == None:
							self.HookV(x, y)
		self.best_words.sort(key=lambda tup: tup[1], reverse = True)
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

	
	def VerticalWordAtPos(self, x, y):
		start_pos = (x, y)
		working_pos = start_pos	
		forward = False		
		current_word = ""
		while self.in_game.GetLetterOfTileInHolderAtPos(working_pos) != None or not forward:
			current_word += self.in_game.GetLetterOfTileInHolderAtPos(working_pos)
			if not forward:
				working_pos = (working_pos[0], working_pos[1] - 1)
				if working_pos[1] < 0 or self.in_game.GetLetterOfTileInHolderAtPos(working_pos) == None:
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
		
		
	def HookV(self, x, y, start_pos = None, forward = False, word = "", tile_placed = False, poss_list = None):
		if poss_list == None:
			poss_list = []		
		if start_pos == None:
			start_pos = (x, y)
			
		try:
			letter = self.in_game.GetLetterOfTileInHolderAtPos((x, y))
			word += letter
		except:
			print (x, y, word, letter)
		#print ("V", word)
		if tile_placed and self.gaddag.checkIsWord(word) and len(word) >= 0 and word[-1] != "@" and ((forward and y == 14) or (forward and y < 14 and self.in_game.GetLetterOfTileInHolderAtPos((x, y + 1)) == None) or (not forward and y == 0) or (not forward and y > 0 and self.in_game.GetLetterOfTileInHolderAtPos((x, y - 1)) == None)):
			#print ("Vsubmit", word)
			score = self.in_game.CalculateWordScore()
			self.best_words.append((tuple(poss_list), score))
		if y > 0 and not forward:
			y -= 1
		elif y == 0 and not forward:
			if start_pos[1] < 14:
				forward = True
				y = start_pos[1] + 1
				word += "@"
			else:
				return
		elif y < 14 and forward:
			y += 1
		elif y >= 14 and forward:
			return
		elif y < 0:
			raise
		
		#next_letter = self.in_game.GetLetterOfTileInHolderAtPos((x, y))
		while True:
			next_letter = self.in_game.GetLetterOfTileInHolderAtPos((x, y))
			#if not forward and next_letter != None:
			if next_letter != None:
				self.HookV(x, y, start_pos, forward, word, tile_placed, poss_list)
			else:
				for rack_pos in range(7):
					rack_letter = self.rack[rack_pos]
					if rack_letter != None:
						rack_letter = self.rack[rack_pos][0]
						if rack_letter == "*":
							for test_letter in self.alphabet:
								#print ("V", word)
								#print (self.gaddag.navigateToNode(word + rack_letter) != None, word + test_letter, forward)
								if self.gaddag.navigateToNode(word + test_letter) != None:
									self.in_game.MoveRackTileToBoard(rack_pos, (x, y), test_letter)
									if self.HorizontalWordAtPos(x, y):
										poss_list.append((rack_pos, (x, y), test_letter))
										self.HookV(x, y, start_pos, forward, word, True, poss_list)
										poss_list.pop(-1)
									self.in_game.MoveBoardTileToRack((x, y), rack_pos)
						else:
							#print ("V", word)
							#print (self.gaddag.navigateToNode(word + rack_letter) != None, word + rack_letter, forward)
							if self.gaddag.navigateToNode(word + rack_letter) != None:
								self.in_game.MoveRackTileToBoard(rack_pos, (x, y))
								if self.HorizontalWordAtPos(x, y):
									poss_list.append((rack_pos, (x, y)))
									self.HookV(x, y, start_pos, forward, word, True, poss_list)
									poss_list.pop(-1)
								self.in_game.MoveBoardTileToRack((x, y), rack_pos)

			if not forward and start_pos[1] < 14 and next_letter == None:
				#print ("hi")
				forward = True
				y = start_pos[1] + 1
				word += "@"
			else:
				break
			#self.HookV(x, y, start_pos, forward, word, tile_placed, poss_list)
			
		
	def HookH(self, x, y, start_pos = None, forward = False, word = "", tile_placed = False, poss_list = None):
		if poss_list == None:
			poss_list = []		
		if start_pos == None:
			start_pos = (x, y)
			
		try:
			letter = self.in_game.GetLetterOfTileInHolderAtPos((x, y))
			word += letter
		except:
			#for n in self.in_game.the_board:
				#print (n)
				#print ("")
			#print ("")
			#print (x, y, word, letter)
			raise
			
		#print ("H", word)
		if tile_placed and self.gaddag.checkIsWord(word) and len(word) >= 1 and word[-1] != "@" and ((forward and x == 14) or (forward and self.in_game.GetLetterOfTileInHolderAtPos((x + 1, y)) == None) or ((not forward and x == 0)) or (not forward and x > 0 and self.in_game.GetLetterOfTileInHolderAtPos((x - 1, y)) == None)):
			#print ("Hsubmit", word)
			score = self.in_game.CalculateWordScore()
			self.best_words.append((tuple(poss_list), score))	
			
		if x > 0 and not forward:
			x -= 1
		elif x == 0 and not forward:
			if start_pos[0] < 14:
				forward = True
				x = start_pos[0] + 1
				word += "@"
			else:
				return
		elif x < 14 and forward:
			x += 1
		elif x >= 14 and forward:
			return
		elif x < 0:
			raise
			
		#next_letter = self.in_game.GetLetterOfTileInHolderAtPos((x, y))
		while True:			
			next_letter = self.in_game.GetLetterOfTileInHolderAtPos((x, y))
			#if not forward and next_letter != None:
			if next_letter != None:
				self.HookH(x, y, start_pos, forward, word, tile_placed, poss_list)
			else:
				for rack_pos in range(7):
					rack_letter = self.rack[rack_pos]
					if rack_letter != None:
						rack_letter = self.rack[rack_pos][0]
						if rack_letter == "*":
							for test_letter in self.alphabet:
								if self.gaddag.navigateToNode(word + test_letter) != None:
									#print ("H", word)
									#print (self.gaddag.navigateToNode(word + rack_letter) != None, word + test_letter, forward)
									self.in_game.MoveRackTileToBoard(rack_pos, (x, y), test_letter)
									if self.VerticalWordAtPos(x, y):
										poss_list.append((rack_pos, (x, y), test_letter))
										self.HookH(x, y, start_pos, forward, word, True, poss_list)
										poss_list.pop(-1)
									self.in_game.MoveBoardTileToRack((x, y), rack_pos)
						else:
							#print ("H", word)
							#print (self.gaddag.navigateToNode(word + rack_letter) != None, word + rack_letter, forward)
							if self.gaddag.navigateToNode(word + rack_letter) != None:
								self.in_game.MoveRackTileToBoard(rack_pos, (x, y))
								if self.VerticalWordAtPos(x, y):
									poss_list.append((rack_pos, (x, y)))
									self.HookH(x, y, start_pos, forward, word, True, poss_list)
									poss_list.pop(-1)
								self.in_game.MoveBoardTileToRack((x, y), rack_pos)
								
			if (not forward) and start_pos[0] < 14 and next_letter == None:
				#print ("hi")
				forward = True
				x = start_pos[0] + 1
				word += "@"
			else:
				break
		
	
	def PlaceLetters(self, pos_struct_tuple):
		for pos_pair in pos_struct_tuple[0]:
			#print (self.rack[pos_pair[0]], pos_pair[1])
			if len(pos_pair) == 2:
				self.in_game.MoveRackTileToBoard(pos_pair[0], pos_pair[1])
			elif len(pos_pair) == 3:
				self.in_game.MoveRackTileToBoard(pos_pair[0], pos_pair[1], pos_pair[2])
			else:
				raise	

	def MakePlay(self):
		self.FindBestWord()
		if len(self.best_words) > 0:
			best_word = self.best_words[0]
		else:
			best_word = None
		#print ("------------------------")
		#print ("rack: ", self.rack)
		if best_word != None:
			self.PlaceLetters(best_word)
			self.best_words.clear()
			"""
			for n in self.in_game.the_board:
				for m in n:
					print (m[0], end = " | ")
				print ("\n")
			print ("")
			"""
			self.in_game.SubmitWord()
		else:
			self.in_game.PassTurn()	
	

