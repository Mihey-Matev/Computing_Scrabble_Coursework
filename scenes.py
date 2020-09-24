import pygame
import visual_elements as VE

# The abstract scene class which controls most events for a specific scene; I decided to have multiple scenes instead of multiple buttons, as doing this makes the process much easier and more intuitive.
class Scene: 
	#def __init__(self, screen):
		#self.screen = screen
 
	def ProcessInput(self, events):#, pressed_keys):
		"""Called when a specific event is detected in the loop."""
		#pass
		raise NotImplementedError("ProcessInput abstract method must be defined in subclass.")

	def Update(self):
		"""Called from the director and defined on the subclass."""
		# Game logic would go here		
		#pass
		raise NotImplementedError("OnUpdate abstract method must be defined in subclass.")
	
	def Draw(self):#, screen):
		"""called when you want to draw the screen."""
		#pass
		raise NotImplementedError("OnDraw abstract method must be defined in subclass.")


# a subclass of scene which is just the main menu as described previously in my document. It contains the buttons to change scenes or exit game along with the game's name.
class MainMenuScene(Scene):
	def __init__(self):#, screen):
		#super(MainMenuScene, self).__init__(screen)
		centre_of_screen = (pygame.display.get_surface().get_size()[0] / 2, pygame.display.get_surface().get_size()[1] / 2)
		
		
		width = pygame.display.get_surface().get_size()[0] * 0.23
		height = pygame.display.get_surface().get_size()[1] * (1.0/7.7)
		spacing = height * (1.0/6.0)
		
		text_size = int(pygame.display.get_surface().get_size()[0] * (7.0/160.0))
		text_colour = (0, 0, 0)
		
		colour = (161,111,80)
		outline_colour = (109, 67, 19)
		total_spacing = height + spacing
		
		#screen = pygame.display.get_surface()
		
		#coordinates of top button
		x = centre_of_screen[0] - 0.5 * width
		y = centre_of_screen[1] - 2 * height + 2.5 * spacing
		
		
		self.VS_AI_btn = VE.Button(colour, x, y, width, height, outline_colour, "VS. AI", text_size, text_colour)
		self.VS_Player_btn = VE.Button(colour, x, y + total_spacing, width, height, outline_colour, "VS. Player", text_size, text_colour)
		self.online_btn = VE.Button(colour, x, y + 2 * total_spacing, width, height, outline_colour, "Online", text_size, text_colour)
		self.exit_game_btn = VE.Button((43, 19, 3), x, y + 3 * total_spacing, width, height, outline_colour, "Exit Game", text_size, (161,111,80))
			
		self.my_buttons = [self.VS_AI_btn, self.VS_Player_btn, self.online_btn, self.exit_game_btn]
	
	def ProcessInput(self, events):
        for button in self.my_buttons:
            button.IsOver(pygame.mouse.get_pos())
		for event in events:
			if event.type == pygame.MOUSEBUTTONDOWN:
				if self.VS_AI_btn.IsOver(pygame.mouse.get_pos()):
					# change to vs ai next scene
					pass
					
				elif self.VS_Player_btn.IsOver(pygame.mouse.get_pos()):
					# change to vs player next scene
					return VSPlayerTransitionScene()#self.screen)
				
				elif self.online_btn.IsOver(pygame.mouse.get_pos()):
					# change to vs online next scene
					pass
				
				elif self.exit_game_btn.IsOver(pygame.mouse.get_pos()):
					# exit game
					pass				
									
	
	def Update(self):
		pass

	
	def Draw(self):#, screen = None):
		#if screen is None:
		#	screen = self.screen
		
		#pygame.display.get_surface().fill((237, 180, 127))
		for button in self.my_buttons:
			button.Draw()#screen)

			
			
			
class VSPlayerTransitionScene(Scene):
	def __init__(self):#, screen):
		pass
		#super(VSPlayerTransitionScene, self).__init__(screen)
		
	def ProcessInput(self, events):#, pressed_keys):
		"""Called when a specific event is detected in the loop."""
		#pass
		raise NotImplementedError("ProcessInput abstract method must be defined in subclass.")

	def Update(self):
		pass
	
	def Draw(self):#, screen):
		"""called when you want to draw the screen."""
		#pass
		raise NotImplementedError("OnDraw abstract method must be defined in subclass.")

