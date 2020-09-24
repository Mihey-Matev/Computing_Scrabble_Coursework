import pygame
import AI
import Player
import Button as Btn
import TextBox
import Rack
#import TileBag
import OnlineGame
import Scene
import Board
import Game
import GameSceneButtons as GSBtns

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
		tile_size = self.the_board.GetTileSize()
		self.the_rack = self.AddVONonBtn(Rack.Rack(tile_width = tile_size[0], tile_height = tile_size[1]), (0.25 * self.width, board_position[1] + 0.5 * board_height - 5 * tile_size[1]))
		"""
		self.clicked_rack_tile = None
		self.clicked_board_tile = None
		"""
		
		# Creation of the other buttons for this scene
		self.submit_btn = Btn.Button(colour = (161,111,80), position = (0, 0), width = self.width/7, height = 3 * tile_size[1] / 2, outline_colour = (109, 67, 19), text = "Submit Word", text_size = 30, text_colour = (0, 0, 0), fade_value = 20)
		self.AddButton(position = (board_position[0] + 0.5 * (board_width - self.submit_btn.GetSize()[0]), 1.25 * self.submit_btn.GetSize()[1] + board_height), button = self.submit_btn)
		
		button_width = self.width / 10.971428571
		button_height = self.height / 17.28
		self.game_scene_btns = GSBtns.GameSceneButtons(button_width = button_width, button_height = button_height)
		self.AddVONonBtn(self.game_scene_btns, (self.the_rack.GetPosition()[0] - 1.6 * self.game_scene_btns.GetSize()[0], board_position[1] + 0.5 * board_height - 3.5 * button_height))
		
		
		# Creation of text boxes with player names and scores
		self.player_box_name_1 = self.AddVONonBtn(TextBox.TextBox(position = (self.game_scene_btns.GetPosition()[0] + 0.4 * button_width, board_position[1] + 0.5 * tile_size[0]), text = "WWWWWWWWWWWW", font_size = round(0.6 * tile_size[0])))
		self.player_box_scoretext_1 = self.AddVONonBtn(TextBox.TextBox(position = (self.player_box_name_1.GetPosition()[0], self.player_box_name_1.GetPosition()[1] + 1.2 * self.player_box_name_1.GetSize()[1]), text = "Score: ", font_size = round(0.6 * tile_size[0])))
		self.player_box_scorenum_1 = self.AddVONonBtn(TextBox.TextBox(position = (self.player_box_scoretext_1.GetPosition()[0] + self.player_box_scoretext_1.GetSize()[0], self.player_box_scoretext_1.GetPosition()[1]), text = 888, font_size = round(0.6 * tile_size[0])))
		
		self.player_box_name_2 = self.AddVONonBtn(TextBox.TextBox(position = (board_position[0] + board_width + 0.5 * tile_size[0], board_position[1] + 0.5 * tile_size[0]), text = "WWWWWWWWWWWW", font_size = round(0.6 * tile_size[0])))
		self.player_box_scoretext_2 = self.AddVONonBtn(TextBox.TextBox(position = (self.player_box_name_2.GetPosition()[0], self.player_box_name_2.GetPosition()[1] + 1.2 * self.player_box_name_2.GetSize()[1]), text = "Score: ", font_size = round(0.6 * tile_size[0])))
		self.player_box_scorenum_2 = self.AddVONonBtn(TextBox.TextBox(position = (self.player_box_scoretext_2.GetPosition()[0] + self.player_box_scoretext_2.GetSize()[0], self.player_box_scoretext_2.GetPosition()[1]), text = 888, font_size = round(0.6 * tile_size[0])))
		
		# gameplay variables
		self.TilePlacementLocations = []
		self.rack_selection = None
		self.board_selection = None		
		
		self.BeforeEachTurn()
		
		
	def PassTurn(self):
		pass
	
	
	def SwapTiles(self):
		pass
	
	
	def ShuffleTiles(self):
		pass
	
	
	def Resign(self):
		pass
	
	
	#def MoveTileTo(self, from_holder, to_holder):		
	#	if from_holder.MoveTileTo(to_holder):
	#		if 
	
		
	def ProcessInput(self, events):		
		self.events = events
		
		# dealing with misc. buttons
		clicked_btn_num = self.game_scene_btns.ProcessInput(events)
		if clicked_btn_num == 0:			
			self.DisplayRemainingTiles(self.the_game.GetRemainingTilesForCurrentPlayer())
		elif clicked_btn_num == 1:
			self.PassTurn()
		elif clicked_btn_num == 2:
			self.SwapTiles()
		elif clicked_btn_num == 3:
			self.ShuffleTiles()
		elif clicked_btn_num == 4:
			self.Resign()
		
		# Dealing with buttons that belong to the scene explicitly
		btn_clicked = self.ButtonClicked()
		if btn_clicked == self.submit_btn:
			#self.the_game.SubmitWord()
			if self.the_game.SubmitWord():
				self.SubmitWord()
			
			
		#self.selected_tile = None
		self.rack_tileholder_clicked_last = None
		
		# getting the tile which was clicked on the rack
		rack_selection_check = self.the_rack.ProcessInput(events)
		if rack_selection_check != None and (rack_selection_check[0].HasTile() or self.board_selection != None or self.rack_selection != None):	# this means the tile was clicked on this frame
			if self.rack_selection == None:
				self.rack_selection = rack_selection_check
				self.rack_tileholder_clicked_last = True
			elif self.rack_selection[0].MoveTileTo(rack_selection_check[0]):
				self.CancelMoves()
			else:
				self.CancelMoves()
		
		# getting the tile which was clicked on the board
		board_selection_check = self.the_board.ProcessInput(events)
		if board_selection_check != None and (board_selection_check[0].HasTile() or self.board_selection != None or self.rack_selection != None):
			if self.board_selection == None:
				self.board_selection = board_selection_check
				self.rack_tileholder_clicked_last = False
			elif self.board_selection[0].MoveTileTo(board_selection_check[0]):
				self.TilePlacementLocations[self.TilePlacementLocations.index(self.board_selection[1])] = board_selection_check[1]
				self.CancelMoves()
			else:
				self.CancelMoves()
		
		# Take action (i.e. move tile) based on above checks
		print ("--------------")
		print (self.rack_selection)
		print (self.board_selection)
		print (self.TilePlacementLocations)
		print ("--------------")
		if self.rack_selection != None and self.rack_selection[0] != None and self.board_selection != None and self.board_selection[0] != None:			
			if self.rack_tileholder_clicked_last:
				if self.board_selection[0].MoveTileTo(self.rack_selection[0]):
					self.TilePlacementLocations.remove(self.board_selection[1])
			elif self.rack_selection[0].MoveTileTo(self.board_selection[0]):
				self.TilePlacementLocations.append(self.board_selection[1])					
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
	
	# can be called to make it so that no tiles are going to be moved
	def CancelMoves(self):
		self.board_selection = None
		self.rack_selection = None
		self.the_game.CancelTileSelection()
	
	
	def DisplayRemainingTiles(self, letters_dict):
		pass
	
	
	def SubmitWord(self):
		for holder in self.TilePlacementLocations:
			self.the_board.GetTileAtPos(holder[0], holder[1]).Deactivate()
		# lock all tiles which were just placed down, then ...
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
		self.TilePlacementLocations.clear()
		
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
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	