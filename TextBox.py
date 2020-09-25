import pygame
import VisualObject as VO

class TextBox(VO.VisualObject):
	def __init__(self, position = (0, 0), text = "", font_size = 30, font_family = "arial", text_colour = (0, 0, 0)):
		self.text_colour = text_colour
		self.font = pygame.font.SysFont(font_family, int(font_size))		
		self.the_text = self.font.render(str(text), 1, self.text_colour)
		self.SetPosition(position)
		self.text = str(text)
		self.position = position
		
	# uses pygame to draw the text
	def Draw(self, surface):
		surface.blit(self.the_text, self.position)		
	
	def SetPosition(self, position):
		self.position = position	
		
	def GetSize(self):
		return (self.the_text.get_width(), self.the_text.get_height())
	
	def SetText(self, text):
		self.the_text = self.font.render(str(text), 1, self.text_colour)
		self.text = text
	
	def GetText(self):
		return self.text
	
	# if used in the context of a string, then use its self.text attribute
	def __str__(self):
		return self.text
		