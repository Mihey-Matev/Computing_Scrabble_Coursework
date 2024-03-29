import pygame
import Scene
import Button as Btn
import GetUsernameScene
import TextBox

# a subclass of scene which is just the main menu as described previously in my document. It contains the buttons to change scenes or exit game along with the game's name.
class MainMenuScene(Scene.Scene):
	def __init__(self, width, height):
		super(MainMenuScene, self).__init__(width, height)
		centre_of_screen = (width / 2, height / 2)
		
		# Button attributes
		width = pygame.display.get_surface().get_size()[0] * 0.23
		height = pygame.display.get_surface().get_size()[1] * (1.0/7.7)
		spacing = height * (1.0/6.0)		
		text_size = int(self.width * (7.0/160.0))
		text_colour = (0, 0, 0)		
		colour = (161,111,80)
		outline_colour = (109, 67, 19)
		total_spacing = height + spacing		
		#coordinates of top button
		x = centre_of_screen[0] - 0.5 * width
		y = centre_of_screen[1] - 2 * height + 2.5 * spacing

		self.VS_AI_btn = self.AddButton(colour, (x, y), width, height, outline_colour, "VS. AI", text_size, text_colour)		
		self.VS_Player_btn = self.AddButton(colour, (x, y + total_spacing), width, height, outline_colour, "VS. Player", text_size, text_colour)
		self.online_btn = self.AddButton(colour, (x, y + 2 * total_spacing), width, height, outline_colour, "Online", text_size, text_colour)
		self.exit_game_btn = self.AddButton((43, 19, 3), (x, y + 3 * total_spacing), width, height, outline_colour, "Exit Game", text_size, (161,111,80))
		
		self.game_name_txt = self.AddText((0, 0), "Words With Friends", text_size * 2, "arial", (0, 0, 0))
		self.game_name_txt.SetPosition((x - 0.33 * self.game_name_txt.GetSize()[0], y - 1.25 * total_spacing))
		
	
	def ProcessInput(self, events):
		self.events = events
		
		btn_clicked = self.ButtonClicked()
		
		if btn_clicked == self.VS_AI_btn:
			return 1
		elif btn_clicked == self.VS_Player_btn:
			return 2
		elif btn_clicked == self.online_btn:
			return 3
		elif btn_clicked == self.exit_game_btn:
			return 4
		
	def Update(self):
		pass

