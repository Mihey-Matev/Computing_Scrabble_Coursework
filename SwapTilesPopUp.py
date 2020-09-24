import pygame
import Button as Btn
import VisualObject as VO

class SwapTilesPopUp(VO.VisualObject):
	def __init__(self, position, width = 500, height = 500, colour = (217, 160, 107)):
		self.colour = colour
		self.width = width
		self.position = position
		self.height = height
		self.cancel_btn = Btn.Button(
				colour = (137, 80, 27),
				position = (self.position[0] + 0.1 * self.width, position[1] + self.height - 0.25 * self.height),
				width = 0.8 * self.width, 
				height = 0.15 * self.height, 
				outline_colour = (187, 130, 77), 
				text = "Cancel", 
				text_size = int(0.2 * self.height * 0.55), 
				text_colour = (0, 0, 0), 
				fade_value = 20,
				is_active = True,
				outline_size = 4)
		self.submit_btn = Btn.Button( 
				colour = (137, 80, 27),
				position = (self.position[0] + 0.1 * self.width,  position[1] + 0.1 * self.height),
				width = 0.8 * self.width, 
				height = 0.15 * self.height, 
				outline_colour = (187, 130, 77), 
				text = "Submit", 
				text_size = int(0.2 * self.height * 0.55), 
				text_colour = (0, 0, 0), 
				fade_value = 20,
				is_active = True,
				outline_size = 4)		
		
	def Draw(self, surface):
		pygame.draw.rect(surface, self.colour, (self.position, (self.width, self.height)), 0)
		self.cancel_btn.Draw(surface)
		self.submit_btn.Draw(surface)		
	
	def SetPosition(self, position):
		super(SwapTilesPopUp, self).SetPosition(position)
		self.cancel_btn.SetPosition((self.cancel_btn.GetPosition()[0] + position[0] - self.position[0], self.cancel_btn.GetPosition()[1] + position[1] - self.position[1]))
		self.submit_btn.SetPosition((self.submit_btn.GetPosition()[0] + position[0] - self.position[0], self.submit_btn.GetPosition()[1] + position[1] - self.position[1]))		
		
	def ProcessInput(self, events):
		self.events = events
		self.cancel_btn.IsOver(pygame.mouse.get_pos())		
		self.submit_btn.IsOver(pygame.mouse.get_pos())
		
		for event in self.events:
			if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
				if self.cancel_btn.IsOver(pygame.mouse.get_pos()):
					return False
				if self.submit_btn.IsOver(pygame.mouse.get_pos()):
					return True
					