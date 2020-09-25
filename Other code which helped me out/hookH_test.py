def HookH(self, x, y, start_pos = None, forward = False, word = "", tile_placed = False, poss_list = None):
		if poss_list == None:
			poss_list = []		
		if start_pos == None:
			start_pos = (x, y)
			
		#print ("hi from HookH")
		#print (self)
		letter = self.in_game.GetLetterOfTileInHolderAtPos((x, y))
		if letter != None:
			word += letter
		
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
		if tile_placed and self.gaddag.checkIsWord(word) and ((forward and self.in_game.GetLetterOfTileInHolderAtPos((x + 1, y)) == None) or (not forward and self.in_game.GetLetterOfTileInHolderAtPos((x - 1, y)) == None)):
			#self.best_words.append((word, score, start_pos, "H"))
			score = self.in_game.CalculateWordScore()
			self.best_words.append((tuple(poss_list), score))
			
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
		print (x, y, word)
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
								self.in_game.MoveBoardTileToRack((x, y), rack_pos)
					else:
						#print (type(word))
						if self.gaddag.navigateToNode(word + rack_letter) != None:
							self.in_game.MoveRackTileToBoard(rack_pos, (x, y))
							if self.VerticalWordAtPos(x, y):
								poss_list.append((rack_pos, (x, y)))
								self.HookH(x, y, start_pos, forward, word, True, poss_list)
							self.in_game.MoveBoardTileToRack((x, y), rack_pos)			
					moved = True
		#self.in_game.GetLetterOfTileInHolderAtPos((x, y))
		#if not moved and not forward:
		#	forward = True
		if not "@" in word:
			self.HookH(start_pos[0] + 1, y, start_pos, True, word + "@", True, poss_list)
		#elif not moved and forward:
		if not moved and forward:
			return
		