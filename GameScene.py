import pygame
import AI
import SwapTilesPopUp
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

# This class is just an interface for the Game class; it doesn't do much 'thinking' of its own, and mainly gives the input to the Game class object (self.the_game) in a way which it can'understand'
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
		
		# panels for special events (such as choosing the letter of a wildcard tile, swapping tiles, showing remaining tiles)
		self.swap_tiles = self.AddVONonBtn(SwapTilesPopUp.SwapTilesPopUp(width = self.width/7, height = self.tile_size[1] * 10, position = (0.25 * self.width + self.tile_size[0] * 2, board_position[1] + 0.5 * board_height - 5 * self.tile_size[1])), (0.25 * self.width + self.tile_size[0] * 2, board_position[1] + 0.5 * board_height - 5 * self.tile_size[1]), True, False)
		self.show_tilebag = self.AddVONonBtn(TileBagPopUp.TileBagPopUp(width = self.tile_size[0] * 15.5, height = self.tile_size[0] * 8, tile_width = self.tile_size[1], tile_height = self.tile_size[1], position = (self.width * 0.35 , self.height * 0.5 - 3.5 * self.tile_size[0])), (self.width * 0.35 , self.height * 0.5 - 3.5 * self.tile_size[0]), True, False)
		self.choose_wildcard_interface = self.AddVONonBtn(WildcardPicker.WildcardPicker(width = self.tile_size[0] * 16, height = self.tile_size[0] * 7, tile_width = self.tile_size[1], tile_height = self.tile_size[1], position = (self.width * 0.35 , self.height * 0.5 - 3.5 * self.tile_size[0])), (self.width * 0.35 , self.height * 0.5 - 3.5 * self.tile_size[0]), True, False)
		
		# gameplay variables
		self.winner = None		# the name of the winner
		self.tile_placement_locations = []	# stores the location on the board of moves tiles; makes dealing with returning all tiles back to the rack easier (deterministic)
		# the following two variables are intermediate variables for when I want to mvoe a tile from one place to another
		self.rack_selection = None		
		self.board_selection = None		
		self.deactivated_tile = None
		
		self.BeforeEachTurn()
			
	def PassTurn(self):
		self.the_rack.CoverRack()
		self.ReturnMovedTilesToRack()
		
		self.Draw()
		pygame.display.update()
		pygame.time.wait(500)
		self.the_game.PassTurn()
		self.BeforeEachTurn()
	
	# puts the tiles which have been moved this turn back onto the rack
	def ReturnMovedTilesToRack(self):
		for pos in self.tile_placement_locations:
			self.the_board.GetHolderAtPos(pos[0], pos[1]).RemoveTile()
		self.tile_placement_locations.clear()
		self.the_game.ReturnMovedTilesToRack()
		self.the_rack.PopulateRack(self.the_game.GetCurrentPlayerLetterTiles())
	
	# both puts the tiles which have been moved this turn back onto the rack, and shuffles them
	def ShuffleTiles(self):
		self.ReturnMovedTilesToRack()
		self.the_game.ShuffleTiles()
		self.the_rack.PopulateRack(self.the_game.GetCurrentPlayerLetterTiles())
	
	# the player which resigns loses, so the winning player wins, and this is reflected by changing the variable self.winner (which is checked for in ProcessInput())
	def Resign(self):
		self.winner = self.the_game.Resign()
			
			
	# this method draws a panel which announces the winner which stays active for some period of time
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
	
	# this method is where all calculations take palce
	def ProcessInput(self, events):								
		if self.winner != None:		# firstly we check if there was a winner; if there was, we announce the winner, and end the game
			self.CongratulateWinner()
			return True
				
		self.events = events
		
		# dealing with buttons which are events which can happen in a scrabble game.
		if not self.game_scene_btns in self.uninteractive_VOs:		# each time there is a check such as this, it is to make sure that the visual object has not been disabled, as if it has, then we shouldn't be abble to interact with it.
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
		
		# Dealing with buttons that belong to the scene explicitly (i.e. only the Submit Word button). If it was clicked, then we firstly check if the logical game agrees with the input, and if it does, we go through with the events for a valid word submission.
		btn_clicked = self.ButtonClicked()
		if btn_clicked == self.submit_btn:
			if self.the_game.SubmitWord():
				self.SubmitWord()
			
		self.rack_tileholder_clicked_last = None
		
		# getting the tile which was clicked on the rack
		if not self.the_rack in self.uninteractive_VOs:
			rack_selection_check = self.the_rack.ProcessInput(events)
			if rack_selection_check != None and (rack_selection_check[0].HasTile() or self.board_selection != None or self.rack_selection != None):	# this means the tile was clicked on this frame
				if self.rack_selection == None:
					self.rack_selection = rack_selection_check
					if self.deactivated_tile == None:
						self.deactivated_tile = self.rack_selection[0].GetTile()
						if self.deactivated_tile != None:
							self.deactivated_tile.Deactivate()
					self.rack_tileholder_clicked_last = True
				elif self.rack_selection[0].MoveTileTo(rack_selection_check[0]):	# moving a lettertile around the rack (graphically)
					self.the_game.MoveRackTileToRackPos(self.rack_selection[1], rack_selection_check[1])	# the logical movement
					self.CancelMoves()
				else:
					self.CancelMoves()
		
		# getting the tile which was clicked on the board
		if not self.the_board in self.uninteractive_VOs:
			board_selection_check = self.the_board.ProcessInput(events)
			if board_selection_check != None and (board_selection_check[0].HasTile() or self.board_selection != None or self.rack_selection != None):
				if self.board_selection == None:
					self.board_selection = board_selection_check
					if self.deactivated_tile == None:
						self.deactivated_tile = self.board_selection[0].GetTile()
						if self.deactivated_tile != None:
							self.deactivated_tile.Deactivate()
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
				
		# deselection actions other than above ones (such as right clicking etc)
		for event in self.events:
			if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 3):
				self.CancelMoves()

	# function returns the letter which the player chooses for their wildcard
	def ChooseWildCardLetter(self):
		current_uninteractive_VOs = list(self.uninteractive_VOs)		
		self.MakeAllVOsUninteractive()
		self.DisplayVO(self.choose_wildcard_interface)
		self.MakeVOInteractive(self.choose_wildcard_interface)
		self.Draw()		
		
		letter_choice = None
		while letter_choice == None:
			events = pygame.event.get()
			self.Draw()
			pygame.display.update()
			letter_choice = self.choose_wildcard_interface.ProcessInput(events)
			for event in events:
				if event.type == pygame.QUIT:
					self.Quit()
					
		self.uninteractive_VOs = list(current_uninteractive_VOs)
		self.HideVO(self.choose_wildcard_interface)
		self.MakeVOUninteractive(self.choose_wildcard_interface)
		return letter_choice
		
		
	# causes and event to occur which displays all of the tiles which are left in the tilebag
	def DisplayRemainingTiles(self):
		# making it so that the user can only interact with the swap panel and their rack; everything else is disabled.
		current_uninteractive_VOs = list(self.uninteractive_VOs)	# this list is a temporary one helping me to get back to the state which I started in before the event (i.e. where the required elements are interactive)
		self.MakeAllVOsUninteractive()
		self.DisplayVO(self.show_tilebag)
		self.MakeVOInteractive(self.show_tilebag)
		self.Draw()
		
		remaining_tiles = self.the_game.GetRemainingTilesForCurrentPlayer()		# this is a list of all of the letters of tiles which should be displayed
		
		exit = False
		while not exit:
			events = pygame.event.get()
			self.Draw()
			pygame.display.update()
			exit = self.show_tilebag.ProcessInput(events, remaining_tiles)		# loop exits once the 'x' button of the new opened panel has been clicked
			for event in events:
				if event.type == pygame.QUIT:
					self.Quit()
			
		# returns the state of the game to what it was before the event (so that the user can interacr with the board, rack and buttons, but not the panel opened by the event)
		self.uninteractive_VOs = list(current_uninteractive_VOs)
		self.HideVO(self.show_tilebag)
		self.MakeVOUninteractive(self.show_tilebag)
	
	
	# can be called to make it so that no tiles are going to be moved
	def CancelMoves(self):
		if self.deactivated_tile != None:
			self.deactivated_tile.Activate()
			self.deactivated_tile = None
		if self.board_selection != None:			
			self.board_selection = None
		if self.rack_selection != None:
			self.rack_selection = None
		
	
	def SwapTiles(self):
		self.ReturnMovedTilesToRack()
		self.CancelMoves()
		list_of_tiles_to_swap = []		# holds the numbers of the position of tiles in the rack which need to be swapped
		list_of_crosses_for_tiles = []	# a list containing the visual crosses which show the user which tiles they want to swap
		
		# making it so that the user can only interact with the swap panel and their rack; everything else is disabled.
		current_uninteractive_VOs = list(self.uninteractive_VOs)	# this list is a temporary one helping me to get back to the state which I started in before the event (i.e. where the required elements are interactive)
		self.MakeAllVOsUninteractive()
		self.DisplayVO(self.swap_tiles)
		self.MakeVOInteractive(self.swap_tiles)
		self.MakeVOInteractive(self.the_rack)
		self.Draw()		
		
		exit_loop = False
		exit_event = None	# the variable which contains the state in which the loop was exited; either with swap tiles event being cancelled, or submitted. Initially neither.
		
		while not exit_loop:
			events = pygame.event.get()
			rack_selection_check = self.the_rack.ProcessInput(events)			
			exit_event = self.swap_tiles.ProcessInput(events)
			if exit_event != None:
				exit_loop = True
				
			if rack_selection_check != None and rack_selection_check[1] in list_of_tiles_to_swap:		# If the player clicks on a tile in their rack during the event, they either want to swap it out, or remove it from the list of tiles which they want to swap out; we first check if it needs to be removed...
				list_of_crosses_for_tiles.remove(list_of_crosses_for_tiles[list_of_tiles_to_swap.index(rack_selection_check[1])])
				list_of_tiles_to_swap.remove(rack_selection_check[1])
			elif rack_selection_check != None:		# ... then we check if it needs to be added
				list_of_tiles_to_swap.append(rack_selection_check[1])
				list_of_crosses_for_tiles.append(TextBox.TextBox(position = (rack_selection_check[0].GetPosition()[0] + 0.17 * rack_selection_check[0].GetSize()[0], rack_selection_check[0].GetPosition()[1]), text = "X", font_size = int((rack_selection_check[0].GetSize()[0])), font_family = "arial", text_colour = (255, 0, 0)))		# this just draws an 'X' aroudn the tile to symbolise that it is going to be swapped out
			self.Draw()
			for box in list_of_crosses_for_tiles:
				box.Draw(self.surface)
			pygame.display.get_surface().blit(self.surface, (0, 0))
			pygame.display.update()
			for event in events:		# Because this is separate from the main game loop, if the player attempts to exit a game during the event, they're unable to without the following two lines of code
				if event.type == pygame.QUIT:
					self.Quit()
			

		# returns the state of the game to what it was before the event (so that the user can interacr with the board, rack and buttons, but not the panel opened by the event)
		self.uninteractive_VOs = list(current_uninteractive_VOs)
		self.HideVO(self.swap_tiles)
		self.MakeVOUninteractive(self.swap_tiles)
		
		num_of_remaining_tiles = len(self.the_game.GetRemainingTilesForCurrentPlayer())
		if len(list_of_tiles_to_swap) != 0 and exit_event and num_of_remaining_tiles - 7 >= len(list_of_tiles_to_swap):	# for the user to have successfully passed a turn, they must have both selected tiles to swap out, clicked the submit button, and not tried to swap tiles when there are none to swap
			self.the_game.SwapTiles(list_of_tiles_to_swap)
			self.PassTurn()
	
	def SubmitWord(self):
		for holder in self.tile_placement_locations:
			self.the_board.GetHolderAtPos(holder[0], holder[1]).Deactivate()
		for y in range(15):		# this part generates a new lettertile in any position which should have a lettertile in it, but doesn't; this will come in useful once the AI can place tiles down onto the board (which wont be displayed, as the AI will only do it logically)
			for x in range(15):
				if self.the_game.GetTileAtPos(x, y) != None and str(self.the_board.GetHolderAtPos(x, y).GetTile()) != str(self.the_game.GetTileAtPos(x, y)[0]):
					self.the_board.GetHolderAtPos(x, y).PlaceTile(GLetterTile.GLetterTile(
										colour = (215, 215, 0),
										width = self.tile_size[0], 
										height = self.tile_size[1], 
										outline_colour = (100, 100, 0), 
										text = self.the_game.GetTileAtPos(x, y)[0],
										text_size = round(0.49 * self.tile_size[0]), 
										text_colour = (0, 0, 0), 
										fade_value = 30,
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
	
		
	# things that need to happen after each turn consistently (such as swapping which player's rack is shown etc)
	def BeforeEachTurn(self):		
		self.tile_placement_locations.clear()
		
		self.player_box_name_1.SetText(self.the_game.GetCurrentPlayerName())
		self.player_box_scorenum_1.SetText(self.the_game.GetCurrentPlayerScore())
		self.player_box_name_2.SetText(self.the_game.GetNextPlayerName())
		self.player_box_scorenum_2.SetText(self.the_game.GetNextPlayerScore())
		
		self.the_rack.PopulateRack(self.the_game.GetCurrentPlayerLetterTiles())
		self.the_rack.UncoverRack()

	def Update(self):
		pass	
	
	def Quit(self):
		pygame.display.quit()
		pygame.quit()
		raise SystemExit
	
	
	
	
	
	
	
	
	
	
	
	