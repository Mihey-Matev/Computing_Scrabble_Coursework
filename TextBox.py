import pygame
import VisualObject as VO

class TextBox(VO.VisualObject):
	def __init__(self, position = (0, 0), text = "", font_size = 30, font_family = "arial", text_colour = (0, 0, 0)):
		self.text_colour = text_colour
		self.font = pygame.font.SysFont(font_family, font_size)		
		self.the_text = self.font.render(str(text), 1, self.text_colour)
		self.SetPosition(position)
		self.text = text
		
	def Draw(self, surface, position = None):
		# this allows me to draw the button on a different surface with different coordinates, but it will still be interacted with with the main surface's coordinates
		if position is None:
			position = self.position
		surface.blit(self.the_text, position)
		
	def GetSize(self):
		return (self.the_text.get_width(), self.the_text.get_height())
	
	def SetText(self, text):
		self.the_text = self.font.render(str(text), 1, self.text_colour)
		self.text = text
	
	def GetText(self):
		#return self.the_text
		return self.text
	
	def __str__(self):
		return self.text
		