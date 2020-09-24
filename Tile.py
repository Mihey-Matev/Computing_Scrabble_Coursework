import pygame
import TextBox
import Button as Btn		
	
class Tile(Btn.Button):
	def __init__(
				self, 
				colour = (255, 255, 255),
				position = (0, 0),
				width = 50, 
				height = 50, 
				outline_colour = None, 
				text = "", 
				text_size = 20, 
				text_colour = (0, 0, 0), 
				fade_value = 20,
				is_active = True,
				outline_size = 4,
				point_worth = 0):

		super(Tile, self).__init__(colour, position, width, height, outline_colour, text, text_size, text_colour, fade_value, is_active, outline_size)
		
		
		self.point_text = TextBox.TextBox(
									(0, 0),
									str(point_worth),
									int(text_size / 2),
									'arial',
									text_colour
									)
		
	def SetPosition(self, position):
		super(Tile, self).SetPosition(position)
		self.point_text.SetPosition((self.position[0] + 2 * self.width / 3.4, self.position[1] + 2 * self.height / 3))

	
	def Draw(self, surface):
		super(Tile, self).Draw(surface)
		self.point_text.Draw(surface)
		