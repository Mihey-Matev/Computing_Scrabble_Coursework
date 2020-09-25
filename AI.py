import pygame
import Player
import Game	
import GADDAG

class AI(Player.Player):
	def __init__(self, nickname, game, gaddag):
		self.gaddag = gaddag
		super(AI, self).__init__(nickname, game)
		self.best_words = []
		self.alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
	
		
	def FindBestWord(self):
		if self.in_game.GetLetterOfTileInHolderAtPos((7, 7)) == None:
			for rack_pos in range(7):
				rack_tile = self.GetLetterTileAtPosition(rack_pos)
				if rack_tile != None:
					if rack_tile[0] != "*":
						self.in_game.MoveRackTileToBoard(rack_pos, (7, 7))
						self.HookH(x = 7, y = 7, poss_list = [(rack_pos, (7, 7))], tiles_placed = 1)
						self.HookV(x = 7, y = 7, poss_list = [(rack_pos, (7, 7))], tiles_placed = 1)
						self.in_game.MoveBoardTileToRack((7, 7), rack_pos)
					else:
						for letter in self.alphabet:
							self.in_game.MoveRackTileToBoard(rack_pos, (7, 7), letter)
							self.HookH(x = 7, y = 7, poss_list = [(rack_pos, (7, 7), letter)], tiles_placed = 1)
							self.HookV(x = 7, y = 7, poss_list = [(rack_pos, (7, 7), letter)], tiles_placed = 1)
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
		
		
	def HookV(self, x, y, start_pos = None, forward = False, word = "", tiles_placed = 0, poss_list = None, h_tried = False):
		if poss_list == None:
			poss_list = []		
		if start_pos == None:
			start_pos = (x, y)			
		
		letter = self.in_game.GetLetterOfTileInHolderAtPos((x, y))
		word += letter
			
		if tiles_placed and self.gaddag.checkIsWord(word) and len(word) >= 1 and word[-1] != "@" and ((forward and y == 14) or (forward and y < 14 and self.in_game.GetLetterOfTileInHolderAtPos((x, y + 1)) == None) or (not forward and y == 0) or (not forward and y > 0 and self.in_game.GetLetterOfTileInHolderAtPos((x, y - 1)) == None)):
			score = self.in_game.CalculateWordScore()
			self.best_words.append((tuple(poss_list), score))
			
		y_new = y
		if y > 0 and not forward:
			y_new -= 1
		elif y == 0 and not forward:
			if start_pos[1] < 14:
				forward = True
				y_new = start_pos[1] + 1
				word += "@"
			else:
				return
		elif y < 14 and forward:
			y_new += 1
		elif y >= 14 and forward:
			return
		elif y < 0:
			raise
		
		while True:
			next_letter = self.in_game.GetLetterOfTileInHolderAtPos((x, y_new))
			if next_letter != None:
				self.HookV(x, y_new, start_pos, forward, word, tiles_placed, poss_list, h_tried)
			else:
				for rack_pos in range(7):
					rack_letter = self.rack[rack_pos]
					if rack_letter != None:
						rack_letter = self.rack[rack_pos][0]
						if rack_letter == "*":
							for test_letter in self.alphabet:
								if self.gaddag.navigateToNode(word + test_letter) != None:
									self.in_game.MoveRackTileToBoard(rack_pos, (x, y_new), test_letter)
									if self.HorizontalWordAtPos(x, y_new):
										poss_list.append((rack_pos, (x, y_new), test_letter))
										self.HookV(x, y_new, start_pos, forward, word, tiles_placed + 1, poss_list, h_tried)
										poss_list.pop(-1)
									self.in_game.MoveBoardTileToRack((x, y_new), rack_pos)
						else:
							if self.gaddag.navigateToNode(word + rack_letter) != None:
								self.in_game.MoveRackTileToBoard(rack_pos, (x, y_new))
								if self.HorizontalWordAtPos(x, y_new):
									poss_list.append((rack_pos, (x, y_new)))
									self.HookV(x, y_new, start_pos, forward, word, tiles_placed + 1, poss_list, h_tried)
									poss_list.pop(-1)
								self.in_game.MoveBoardTileToRack((x, y_new), rack_pos)
								
						if not h_tried and len(poss_list) == 1 and self.gaddag.checkIsWord(word):
							x_h = poss_list[0][1][0]
							while x_h < 14 and self.in_game.GetLetterOfTileInHolderAtPos((x_h + 1, y)) != None:
								x_h += 1
							#print (poss_list, x_h, y)
							self.HookH(x = x_h, y = y, poss_list = poss_list, v_tried = True)
							poss_list = [poss_list[0]]
							#print ("after call", poss_list)

			if not forward and start_pos[1] < 14 and next_letter == None:
				forward = True
				y_new = start_pos[1] + 1
				word += "@"
			else:
				break
			
		
	def HookH(self, x, y, start_pos = None, forward = False, word = "", tiles_placed = 0, poss_list = None, v_tried = False):
		if poss_list == None:
			poss_list = []		
		if start_pos == None:
			start_pos = (x, y)
			
		letter = self.in_game.GetLetterOfTileInHolderAtPos((x, y))
		word += letter
			
		if tiles_placed and self.gaddag.checkIsWord(word) and len(word) >= 1 and word[-1] != "@" and ((forward and x == 14) or (forward and self.in_game.GetLetterOfTileInHolderAtPos((x + 1, y)) == None) or ((not forward and x == 0)) or (not forward and x > 0 and self.in_game.GetLetterOfTileInHolderAtPos((x - 1, y)) == None)):
			score = self.in_game.CalculateWordScore()
			self.best_words.append((tuple(poss_list), score))	
			
		x_new = x
		if x > 0 and not forward:
			x_new -= 1
		elif x == 0 and not forward:
			if start_pos[0] < 14:
				forward = True
				x_new = start_pos[0] + 1
				word += "@"
			else:
				return
		elif x < 14 and forward:
			x_new += 1
		elif x >= 14 and forward:
			return
		elif x < 0:
			raise
			
		while True:			
			next_letter = self.in_game.GetLetterOfTileInHolderAtPos((x_new, y))
			if next_letter != None:
				self.HookH(x_new, y, start_pos, forward, word, tiles_placed, poss_list, v_tried)
			else:
				for rack_pos in range(7):
					rack_letter = self.rack[rack_pos]
					if rack_letter != None:
						rack_letter = self.rack[rack_pos][0]
						if rack_letter == "*":
							for test_letter in self.alphabet:
								if self.gaddag.navigateToNode(word + test_letter) != None:
									self.in_game.MoveRackTileToBoard(rack_pos, (x_new, y), test_letter)
									if self.VerticalWordAtPos(x_new, y):
										poss_list.append((rack_pos, (x_new, y), test_letter))
										self.HookH(x_new, y, start_pos, forward, word, tiles_placed + 1, poss_list, v_tried)
										poss_list.pop(-1)
									self.in_game.MoveBoardTileToRack((x_new, y), rack_pos)
						else:
							if self.gaddag.navigateToNode(word + rack_letter) != None:
								self.in_game.MoveRackTileToBoard(rack_pos, (x_new, y))
								if self.VerticalWordAtPos(x_new, y):
									poss_list.append((rack_pos, (x_new, y)))
									self.HookH(x_new, y, start_pos, forward, word, tiles_placed + 1, poss_list, v_tried)
									poss_list.pop(-1)
								self.in_game.MoveBoardTileToRack((x_new, y), rack_pos)
						
						if not v_tried and len(poss_list) == 1 and self.gaddag.checkIsWord(word):
							y_v = poss_list[0][1][1]
							while y_v < 14 and self.in_game.GetLetterOfTileInHolderAtPos((x, y_v + 1)) != None:
								y_v += 1
							#print (poss_list, x, y_v)
							self.HookV(x = x, y = y_v, poss_list = poss_list, h_tried = True)
							poss_list = [poss_list[0]]
							#print ("after call", poss_list)
							
								
			if (not forward) and start_pos[0] < 14 and next_letter == None:
				forward = True
				x_new = start_pos[0] + 1
				word += "@"
			else:
				break
		
	
	def PlaceLetters(self, pos_struct_tuple):
		for pos_pair in pos_struct_tuple[0]:
			print (pos_pair)
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
		if best_word != None:
			self.PlaceLetters(best_word)
			self.best_words.clear()
			"""
			for n in self.in_game.the_board:
				for m in n:
					if m[0] == None:
						print ("WPLACEHW", end = " ")
					else:
						print (m[0], end = " ")
				print ("\n")
			"""
			self.in_game.SubmitWord()
		else:
			self.in_game.PassTurn()	
	

