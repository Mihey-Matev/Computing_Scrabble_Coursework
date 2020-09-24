import pygame
import time
import MainMenuScene
import GetUsernameScene
import NotImplementedScene as NIS
import GameScene


class Director: # This class is basically the class which links everything together and controls the whole game
	def __init__(self, theme_colour = (237, 180, 127)):
		pygame.init()
		self.theme_colour = theme_colour
		self.screen = pygame.display.set_mode((int(1920*0.8), int(1080*0.8)))
		pygame.display.set_caption("Scrabble-like Game")
		
		self.background = pygame.Surface(self.screen.get_size())
		self.background = self.background.convert()
		self.background.fill(self.theme_colour)
		
		self.quit_flag = False
		
		self.main_menu_scene = MainMenuScene.MainMenuScene(self.screen.get_size()[0], self.screen.get_size()[1])
		self.not_implemented_scene = NIS.NotImplementedScene(self.screen.get_size()[0], self.screen.get_size()[1])
		self.ChangeToScene(self.main_menu_scene)
		self.MainGameLoop() 
	
	# sets the background colour for the game, so it doesn't have to be done separately by each scene; however, if i scene does want to change the background colour, it still can.
	def BgColourDrawer(self):
		pygame.display.get_surface().fill(self.theme_colour)

	
	# The loop which allows the game to play; it ends only when the user presses the 'x' button or exit game button (in the main menu)
	def MainGameLoop(self): 
		while not self.quit_flag:
			try:	
				# Main Menu loop
				game_option = 0
				self.ChangeToScene(self.main_menu_scene)
				while not game_option:
					game_option = self.RegularSceneEvents()						

				number_of_players = 0
				number_of_AIs = 0
				# each number plays a different game: 1 - VS AI, 2 - Vs Plater, 3 - Online, and 4 is exit game.
				if game_option == 1:
					#self.NotImplementedProcedure()
					#break
					raise NotImplementedError("Section of game not implemented yet")
				elif game_option == 2:
					number_of_players = 2
				elif game_option == 3:
					#self.NotImplementedProcedure()
					#break
					raise NotImplementedError("Section of game not implemented yet") 
				else:
					self.Quit()
					break

				# Instantiation of players/AIs based on above information
				player_names = []
				for n in range(number_of_players):
					self.ChangeToScene(GetUsernameScene.GetUsernameScene(self.screen.get_size()[0], self.screen.get_size()[1]))
					player_names.append(None)
					while not isinstance(player_names[-1], str):
						player_names[-1] = self.RegularSceneEvents()				
				AI_names = []
				for n in range(number_of_AIs):
					AI_names.append("AI " + str(n + 1))

				# In-game loop
				game_over = False
				self.ChangeToScene(GameScene.GameScene(self.screen.get_size()[0], self.screen.get_size()[1], player_names, AI_names))
				while not game_over:
					game_over = self.RegularSceneEvents()
					
					
			# If the user tries to access a part of the game which has not been implemented yet, the game is restarted; mainly aimed at if the user tries to play online or vs ai
			except NotImplementedError as e:
				if str(e) == "Section of game not implemented yet":
					self.NotImplementedProcedure()
				else:
					raise
					
			
 	# Changes the current scene.
	def ChangeToScene(self, scene):		
		self.scene = scene
		
	def NotImplementedProcedure(self):
		self.ChangeToScene(self.not_implemented_scene)		
		self.RegularSceneEvents()
		time.sleep(3)
		self.ChangeToScene(self.main_menu_scene)
		
	def CheckForExitEvents(self):
		for event in self.current_events:
			if event.type == pygame.QUIT:
				self.Quit()
				
	def RegularSceneEvents(self):
		self.current_events = pygame.event.get()
		self.CheckForExitEvents()
		scene_output = self.scene.ProcessInput(self.current_events)

		# Update scene
		self.scene.Update()

		# Draw the screen
		self.BgColourDrawer()
		self.scene.Draw()
		pygame.display.flip()
		
		return scene_output

	def Quit(self):
		self.quit_flag = True
		pygame.display.quit()
		pygame.quit()
		raise SystemExit

