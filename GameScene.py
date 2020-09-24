import pygame
import AI
import Player
import Button as Btn
import TextBox
import Rack
import GLetterTile
import OnlineGame
import Scene
import Board
import Game
import TileBagPopUp
import GameSceneButtons as GSBtns
import WildcardPicker

class GameScene(Scene.Scene):
	def __init__(self, width, height, player_names, AI_names):
		super(GameScene, self).__init__(width, height)
		self.the_game = Game.Game(player_names, AI_names)
		
		# Board size calculations and instantiation
		s_width = pygame.display.get_surface().get_size()[0]
		s_height = pygame.display.get_surface().get_size()[1]		
		board_height = s_height * 0.8
		board_width = board_height
		board_position = (width - s_height * 0.07 - board_width - width * 0.17, s_height * 0.07)
		self.the_board = self.AddVONonBtn(Board.Board(horizontal_tile_num = 15, vertical_tile_num = 15, buffer_around_board = 10, tile_spacing = 4, width = board_width, height = board_height, position = board_position), board_position)
		
		# Rack calculations and instantiation
		self.tile_size = self.the_board.GetTileSize()
		self.the_rack = self.AddVONonBtn(Rack.Rack(tile_width = self.tile_size[0], tile_height = self.tile_size[1]), (0.25 * self.width, board_position[1] + 0.5 * board_height - 5 * self.tile_size[1]))
		"""
		self.clicked_rack_tile = None
		self.clicked_board_tile = None
		"""
		
		# Creation of the other buttons for this scene
		self.submit_btn = Btn.Button(colour = (161,111,80), position = (0, 0), width = self.width/7, height = 3 * self.tile_size[1] / 2, outline_colour = (109, 67, 19), text = "Submit Word", text_size = 30, text_colour = (0, 0, 0), fade_value = 20)
		self.AddButton(position = (board_position[0] + 0.5 * (board_width - self.submit_btn.GetSize()[0]), 1.25 * self.submit_btn.GetSize()[1] + board_height), button = self.submit_btn)
		
		button_width = self.width / 10.971428571
		button_height = self.height / 17.28
		self.game_scene_btns = GSBtns.GameSceneButtons(button_width = button_width, button_height = button_height)
		self.AddVONonBtn(self.game_scene_btns, (self.the_rack.GetPosition()[0] - 1.6 * self.game_scene_btns.GetSize()[0], board_position[1] + 0.5 * board_height - 3.5 * button_height))
		
		
		# Creation of text boxes with player names and scores
		self.player_box_name_1 = self.AddVONonBtn(TextBox.TextBox(position = (self.game_scene_btns.GetPosition()[0] + 0.4 * button_width, board_position[1] + 0.5 * self.tile_size[0]), text = "WWWWWWWWWWWW", font_size = round(0.6 * self.tile_size[0])))
		self.player_box_scoretext_1 = self.AddVONonBtn(TextBox.TextBox(position = (self.player_box_name_1.GetPosition()[0], self.player_box_name_1.GetPosition()[1] + 1.2 * self.player_box_name_1.GetSize()[1]), text = "Score: ", font_size = round(0.6 * self.tile_size[0])))
		self.player_box_scorenum_1 = self.AddVONonBtn(TextBox.TextBox(position = (self.player_box_scoretext_1.GetPosition()[0] + self.player_box_scoretext_1.GetSize()[0], self.player_box_scoretext_1.GetPosition()[1]), text = 888, font_size = round(0.6 * self.tile_size[0])))
		
		self.player_box_name_2 = self.AddVONonBtn(TextBox.TextBox(position = (board_position[0] + board_width + 0.5 * self.tile_size[0], board_position[1] + 0.5 * self.tile_size[0]), text = "WWWWWWWWWWWW", font_size = round(0.6 * self.tile_size[0])))
		self.player_box_scoretext_2 = self.AddVONonBtn(TextBox.TextBox(position = (self.player_box_name_2.GetPosition()[0], self.player_box_name_2.GetPosition()[1] + 1.2 * self.player_box_name_2.GetSize()[1]), text = "Score: ", font_size = round(0.6 * self.tile_size[0])))
		self.player_box_scorenum_2 = self.AddVONonBtn(TextBox.TextBox(position = (self.player_box_scoretext_2.GetPosition()[0] + self.player_box_scoretext_2.GetSize()[0], self.player_box_scoretext_2.GetPosition()[1]), text = 888, font_size = round(0.6 * self.tile_size[0])))
		
		self.show_tilebag = self.AddVONonBtn(TileBagPopUp.TileBagPopUp(width = self.tile_size[0] * 15.5, height = self.tile_size[0] * 8, tile_width = self.tile_size[1], tile_height = self.tile_size[1]), (self.width * 0.35 , self.height * 0.5 - 3.5 * self.tile_size[0]), True, False)
		self.choose_wildcard_interface = self.AddVONonBtn(WildcardPicker.WildcardPicker(width = self.tile_size[0] * 16, height = self.tile_size[0] * 7, tile_width = self.tile_size[1], tile_height = self.tile_size[1]), (self.width * 0.35 , self.height * 0.5 - 3.5 * self.tile_size[0]), True, False)
		
		# gameplay variables
		self.winner = None
		self.tile_placement_locations = []
		self.rack_selection = None
		self.board_selection = None		
		
		self.BeforeEachTurn()
		
		
	def PassTurn(self):
		self.the_rack.CoverRack()
		self.ReturnMovedTilesToRack()
		
		self.Draw()
		pygame.display.update()
		pygame.time.wait(500)
		self.the_game.PassTurn()
		self.BeforeEachTurn()
	
	
	def SwapTiles(self):
		self.ReturnMovedTilesToRack()
		list_of_tiles_to_swap = []
		
		
		self.the_game.SwapTiles(list_of_tiles_to_swap)
		self.PassTurn()
	
	
	def ReturnMovedTilesToRack(self):
		for pos in self.tile_placement_locations:
			self.the_board.GetHolderAtPos(pos[0], pos[1]).RemoveTile()
		self.tile_placement_locations.clear()
		#print (self.the_game.GetCurrentPlayerLetterTiles())
		self.the_game.ReturnMovedTilesToRack()
		self.the_rack.PopulateRack(self.the_game.GetCurrentPlayerLetterTiles())
	
	
	def ShuffleTiles(self):
		self.ReturnMovedTilesToRack()
		self.the_game.ShuffleTiles()
	
	
	def Resign(self):
		self.winner = self.the_game.Resign()
			
			
	def CongratulateWinner(self):
		self.MakeAllVOsUninteractive()
		pygame.draw.rect(self.surface, (192, 135, 82), (self.width * 0.25 , self.height * 0.25, self.width * 0.5, self.height * 0.5), 0)
		announcement_rect = pygame.draw.rect(self.surface, (217, 160, 107), (self.width * 0.26 , self.height * 0.26, self.width * 0.48, self.height * 0.48), 0)
		winner_text_1 = TextBox.TextBox(text = "Congratulations", font_size = int(announcement_rect.width * 0.085), font_family = "arial", text_colour = (0, 0, 0))
		winner_text_2 = TextBox.TextBox(text = str(self.winner) + "!", font_size = int(announcement_rect.width * 0.085), font_family = "arial", text_colour = (0, 0, 0))
		
		winner_text_1.SetPosition((announcement_rect.centerx - 0.5 * winner_text_1.GetSize()[0], announcement_rect.centery - 0.65 * winner_text_1.GetSize()[1]))
		winner_text_2.SetPosition((announcement_rect.centerx - 0.5 * winner_text_2.GetSize()[0], announcement_rect.centery + 0.3 * winner_text_2.GetSize()[1]))
				
		winner_text_1.Draw(self.surface)
		winner_text_2.Draw(self.surface)
		pygame.display.get_surface().blit(self.surface, (0, 0))
		pygame.display.update()		
		self.HideAllVOs()
		pygame.time.wait(3500)		
	
	#def MoveTileTo(self, from_holder, to_holder):		
	#	if from_holder.MoveTileTo(to_holder):
	#		if 
	
		
	def ProcessInput(self, events):								
		if self.winner != None:
			self.CongratulateWinner()
			return True
				
		self.events = events
		
		# dealing with misc. buttons
		if not self.game_scene_btns in self.uninteractive_VOs:
			clicked_btn_num = self.game_scene_btns.ProcessInput(events)
			if clicked_btn_num == 0:			
				self.DisplayRemainingTiles()
			elif clicked_btn_num == 1:
				self.PassTurn()
			elif clicked_btn_num == 2:
				self.SwapTiles()
			elif clicked_btn_num == 3:
				self.ShuffleTiles()
			elif clicked_btn_num == 4:
				self.Resign()
		
		# Dealing with buttons that belong to the scene explicitly (i.e. only the Submit Word button)
		btn_clicked = self.ButtonClicked()
		if btn_clicked == self.submit_btn:
			#self.the_game.SubmitWord()
			if self.the_game.SubmitWord():
				self.SubmitWord()
			
			
		#self.selected_tile = None
		self.rack_tileholder_clicked_last = None
		
		# getting the tile which was clicked on the rack
		if not self.the_rack in self.uninteractive_VOs:
			rack_selection_check = self.the_rack.ProcessInput(events)
			if rack_selection_check != None and (rack_selection_check[0].HasTile() or self.board_selection != None or self.rack_selection != None):	# this means the tile was clicked on this frame
				if self.rack_selection == None:
					self.rack_selection = rack_selection_check
					self.rack_tileholder_clicked_last = True
				elif self.rack_selection[0].MoveTileTo(rack_selection_check[0]):	# moving a lettertile around the rack (graphically)
					self.the_game.MoveRackTileToRackPos(self.rack_selection[1], rack_selection_check[1])	# the logical movement
					self.CancelMoves()
				else:
					self.CancelMoves()
					
		#if not self.choose_wildcard_interface in self.disabled_VOs:
		#	wild_card_choice = self.choose_wildcard_interface.ProcessInput(events)
		
		
		# getting the tile which was clicked on the board
		if not self.the_board in self.uninteractive_VOs:
			board_selection_check = self.the_board.ProcessInput(events)
			if board_selection_check != None and (board_selection_check[0].HasTile() or self.board_selection != None or self.rack_selection != None):
				if self.board_selection == None:
					self.board_selection = board_selection_check
					self.rack_tileholder_clicked_last = False
				elif self.board_selection[0].MoveTileTo(board_selection_check[0]):	# moving a lettertile around the board (graphically)
					wild_card_choice = None
					if int(board_selection_check[0].GetTile()) == 0:	# we can check if a lettertile is a wildcard by checking if its score is zero; when moving it here, we want to set its symbol to whatever the player chooses
						wild_card_choice = self.ChooseWildCardLetter()
						board_selection_check[0].GetTile().SetText(wild_card_choice)
					self.the_game.MoveBoardTileToBoardPos(self.board_selection[1], board_selection_check[1], str(wild_card_choice))	# the logical movement

					self.tile_placement_locations[self.tile_placement_locations.index(self.board_selection[1])] = board_selection_check[1]
					self.CancelMoves()
				else:
					self.CancelMoves()
		
			# Take action (i.e. move tile) based on above checks
			#print ("--------------")
			#print (self.rack_selection)
			#print (self.board_selection)
			#print (self.tile_placement_locations)
			#print ("--------------")
			"""
			for n in self.the_game.the_board:
				for m in n:
					print (str(m[0]) + ", ", end="")
				print ("")
			print ("----------------------------------------------")
			"""
			if self.rack_selection != None and self.rack_selection[0] != None and self.board_selection != None and self.board_selection[0] != None:			
				if self.rack_tileholder_clicked_last:
					if self.board_selection[0].MoveTileTo(self.rack_selection[0]):	# moving a lettertile from the board back to the rack						
						if int(self.rack_selection[0].GetTile()) == 0: 	# we can check if a lettertile is a wildcard by checking if its score is zero; when moving it here, we want to reset its symbol to show its default
							self.rack_selection[0].GetTile().SetText("*")
						self.the_game.MoveBoardTileToRack(self.board_selection[1], self.rack_selection[1])	# the logical movement
						self.tile_placement_locations.remove(self.board_selection[1])
				elif self.rack_selection[0].MoveTileTo(self.board_selection[0]):	# moving a lettertile from the rack onto the board
					wild_card_choice = None
					if int(self.board_selection[0].GetTile()) == 0:	# we can check if a lettertile is a wildcard by checking if its score is zero; when moving it here, we want to set its symbol to whatever the player chooses
						wild_card_choice = self.ChooseWildCardLetter()
						self.board_selection[0].GetTile().SetText(wild_card_choice)
					self.the_game.MoveRackTileToBoard(self.rack_selection[1], self.board_selection[1], str(wild_card_choice))	# the logical movement
					self.tile_placement_locations.append(self.board_selection[1])					
				self.CancelMoves()
				
				
		#self.board_selection = None
		#if not (self.board_selection is None):
		#	self.board_selection = self.board_selection[1]
				
		# deselection actions other than above ones (such as right clicking etc)
		for event in self.events:
			if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 3):
				self.CancelMoves()

		
		
				
	"""
		if self.clicked_rack_tile is None:
			self.clicked_rack_tile = self.the_rack.ProcessInput(events)
		else:			
			self.clicked_board_tile = self.the_board.ProcessInput(events)
			if not (self.clicked_board_tile is None):
				self.clicked_rack_tile.SetPosition(self.clicked_board_tile.GetPosition())
				self.clicked_board_tile.ToggleIsActive()
				
				self.clicked_rack_tile = None
				self.clicked_board_tile = None				
	"""

	# function returns the letter which the player chooses for their wildcard
	def ChooseWildCardLetter(self):
		"""
		return "A"
		"""
		current_uninteractive_VOs = list(self.uninteractive_VOs)		
		self.MakeAllVOsUninteractive()
		self.DisplayVO(self.choose_wildcard_interface)
		self.MakeVOInteractive(self.choose_wildcard_interface)
		self.Draw()		
		
		letter_choice = None
		while letter_choice == None:
			events = pygame.event.get()
			#print (self.disabled_VOs)
			self.Draw()
			letter_choice = self.choose_wildcard_interface.ProcessInput(events)
			#print (str(letter_choice))
					
		#self.MakeAllVOsInteractive()
		self.uninteractive_VOs = list(current_uninteractive_VOs)
		self.HideVO(self.choose_wildcard_interface)
		self.MakeVOUninteractive(self.choose_wildcard_interface)
		return letter_choice
		
	# causes and event to occur which displays all of the tiles which are left in the tilebag
	def DisplayRemainingTiles(self):
		current_uninteractive_VOs = list(self.uninteractive_VOs)
		self.MakeAllVOsUninteractive()
		self.DisplayVO(self.show_tilebag)
		self.MakeVOInteractive(self.show_tilebag)
		self.Draw()
		
		remaining_tiles = self.the_game.GetRemainingTilesForCurrentPlayer()
		
		exit = False
		while not exit:
			events = pygame.event.get()
			self.Draw()
			exit = self.show_tilebag.ProcessInput(events, remaining_tiles)
			
		self.uninteractive_VOs = list(current_uninteractive_VOs)
		self.HideVO(self.show_tilebag)
		self.MakeVOUninteractive(self.show_tilebag)
	
	
	# can be called to make it so that no tiles are going to be moved
	def CancelMoves(self):
		self.board_selection = None
		self.rack_selection = None
		#self.the_game.CancelTileSelection()

	
	def SubmitWord(self):
		for holder in self.tile_placement_locations:
			self.the_board.GetHolderAtPos(holder[0], holder[1]).Deactivate()
		for y in range(15):		# this part generates a new lettertile in any position which should have a lettertile in it, but doesn't; this will come in useful once the AI can place tiles down onto the board (which wont be displayed, as the AI will only do it logically)
			for x in range(15):
				if self.the_game.GetTileAtPos(x, y) != None and str(self.the_board.GetHolderAtPos(x, y).GetTile()) != str(self.the_game.GetTileAtPos(x, y)[0]):
					#print (str(self.the_board.GetHolderAtPos(x, y).GetTile()), self.the_game.GetTileAtPos(x, y))
					self.the_board.GetHolderAtPos(x, y).PlaceTile(GLetterTile.GLetterTile(
										colour = (215, 215, 0),
										width = self.tile_size[0], 
										height = self.tile_size[1], 
										outline_colour = (100, 100, 0), 
										text = self.the_game.GetTileAtPos(x, y)[0],
										text_size = round(0.75 * (self.tile_size[0] - 12)), 
										text_colour = (0, 0, 0), 
										fade_value = 20,
										is_active = False,
										outline_size = 4,
										point_worth = self.the_game.GetTileAtPos(x, y)[1])
										)
				
	
		self.winner = self.the_game.GetWinner()	# check if there is a winner
		if self.winner == None:		# if there is a winner, they would be announced; otherwise, continue with the game.
			self.the_rack.CoverRack()		
			self.Draw()
			pygame.display.update()	
			pygame.time.wait(500)
			self.BeforeEachTurn()
				
	# given a list of the lettertile which remain in the tilebag, creates a visual output for the user to see them
	def DisplayRemainingLetterTiles(self, lettertiles):
		pass
	
		
	# things that need to happen after each turn consistently (such as swapping which player's rack is shown etc)
	def BeforeEachTurn(self):		
		self.tile_placement_locations.clear()
		
		self.player_box_name_1.SetText(self.the_game.GetCurrentPlayerName())
		self.player_box_scorenum_1.SetText(self.the_game.GetCurrentPlayerScore())
		#self.current_player_name = self.the_game.GetCurrentPlayerName()
		#self.current_player_score = self.the_game.GetCurrentPlayerScore()
		#self.current_player_rack = self.GetCurrentPlayerRack()
		#print (self.the_game.GetCurrentPlayerName())
		self.player_box_name_2.SetText(self.the_game.GetNextPlayerName())
		self.player_box_scorenum_2.SetText(self.the_game.GetNextPlayerScore())
		#print (self.the_game.GetNextPlayerName())
		#self.next_player_name = self.the_game.GetNextPlayerName()
		#self.next_player_score = self.the_game.GetNextPlayerScore()
		#self.next_player_rack = self.GetNextPlayerRack()
		
		self.the_rack.PopulateRack(self.the_game.GetCurrentPlayerLetterTiles())
		self.the_rack.UncoverRack()
		
		
		
	def GetNextPlayerRack(self):
		return
	
	
	def GetCurrentPlayerRack(self):
		return

	
	def Update(self):
		# Game logic would go here
		pass
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	