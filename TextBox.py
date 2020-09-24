import pygame
import VisualObject as VO

class TextBox(VO.VisualObject):
	def __init__(self, position = (0, 0), text = "", font_size = 30, font_family = "arial", text_colour = (0, 0, 0)):
		font = pygame.font.SysFont(font_family, font_size)		
		self.the_text = font.render(text, 1, text_colour)
		self.SetPosition(position)
		
	def Draw(self, surface):
		surface.blit(self.the_text, self.position)
		
	def GetSize(self):
		return (self.the_text.get_width(), self.the_text.get_height())
	

		