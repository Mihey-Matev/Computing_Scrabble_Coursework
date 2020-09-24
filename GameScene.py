import pygame
import AI
import Player
import Button as Btn
import TextBox
import Rack
import TileBag
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
		self.the_rack = self.AddVONonBtn(Rack.Rack(tile_width = tile_size[0], tile_height = tile_size[1], lettertile_letters = ["A", "B"]), (0.25 * self.width, board_position[1] + 0.5 * board_height - 5 * tile_size[1]))
		
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
		
	def ProcessInput(self, events):		
		self.events = events
		
		clicked_btn_num = self.game_scene_btns.ProcessInput(events)
		if clicked_btn_num == 0:			
			self.DisplayRemainingTiles(self.the_game.GetRemainingTilesForCurrentPlayer())
		elif clicked_btn_num == 1:
			pass
		elif clicked_btn_num == 2:
			pass
		elif clicked_btn_num == 3:
			pass
		elif clicked_btn_num == 4:
			pass
		
		# Dealing with buttons that belong to the scene explicitly
		btn_clicked = self.ButtonClicked()
		if btn_clicked == self.submit_btn:
			self.the_game.SubmitWord()
			
		clicked_lettertile_num = self.the_rack.ProcessInput(events)
		
		clicked_board_btn = self.the_board.ProcessInput(events)
		clicked_board_btn_pos = None
		if not (clicked_board_btn is None):
			clicked_board_btn_pos = clicked_board_btn[1]
				
		for event in self.events:
			if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
				pass
		
				
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
				
	# given a list of the lettertile which remain in the tilebag, creates a visual output for the user to see them
	def DisplayRemainingLetterTiles(self, lettertiles):
		pass
	
		
	# things that need to happen after each turn consistently (such as swapping which player's rack is shown etc)
	def AfterEachTurn(self):
		self.current_player_name = self.the_game.GetCurrentPlayerName()
		self.current_player_score = self.the_game.GetCurrentPlayerScore()
		self.next_player_name = self.the_game.GetNextPlayerName()
		self.next_player_score = self.the_game.GetNextPlayerScore()

	
	def Update(self):
		# Game logic would go here
		pass
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	