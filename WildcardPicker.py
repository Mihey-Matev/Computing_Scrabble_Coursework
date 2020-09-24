import pygame
import VisualObject as VO
import GLetterTile
import TextBox


class WildcardPicker(VO.VisualObject):
	def __init__(self, width, height, position = (0, 0), tile_width = 50, tile_height = 50, picker_colour = (217, 160, 107)):
		super(WildcardPicker, self).__init__(position)
		self.tile_height = tile_height
		self.tile_width = tile_width
		self.width = width
		self.height = height
		self.picker_colour = picker_colour
		self.instruction_text = TextBox.TextBox(
												position = (0, 0),
												text = "Please select your wildcard letter:",
												font_size = int(tile_width * 0.8),
												font_family = "arial",
												text_colour = (0, 0, 0)
												)
		self.instruction_text.SetPosition((self.position[0] + 0.5 * self.width - 0.5 * self.instruction_text.GetSize()[0], self.position[1] + 0.5 * self.instruction_text.GetSize()[1]))
		
		self.tiles = [GLetterTile.GLetterTile(
											colour = (210, 210, 0),
											position = (self.position[0] + 0.5 * self.tile_width + (n % 10) * 1.5 * (self.tile_width), self.position[1] + self.tile_height * 2 + int(n / 10) * self.tile_height * 1.5),
											width = self.tile_width, 
											height = self.tile_height, 
											outline_colour = (100, 100, 0), 
											text = chr(65 + n),
											text_size = round(0.75 * (self.tile_width - 12)), 
											text_colour = (0, 0, 0), 
											fade_value = 20,
											is_active = True,
											outline_size = 4,
											point_worth = 0
											)
											for n in range(26)]
		

		
	
	def Draw(self, surface):		
		pygame.draw.rect(surface, self.picker_colour, (self.position, (self.width, self.height)), 0)
		self.instruction_text.Draw(surface)		
		for tile in self.tiles:
			tile.Draw(surface)
		pygame.display.update()
	
	
	# returns the letter which was clicked
	def ProcessInput(self, events):
		self.events = events
		the_letter = self.FindClickedLetter()
		#print (the_letter)
		if the_letter != None:
			return the_letter
	
	
	def SetPosition(self, position):
		for tile in self.tiles:
			tile.SetPosition((tile.GetPosition()[0] + position[0] - self.position[0], tile.GetPosition()[1] + position[1] - self.position[1]))
		self.instruction_text.SetPosition((self.instruction_text.GetPosition()[0] + position[0] - self.position[0], self.instruction_text.GetPosition()[1] + position[1] - self.position[1]))
		self.position = position
		
	
	
	def FindClickedLetter(self):
		for tile in self.tiles:
			tile.IsOver(pygame.mouse.get_pos())		
		
		for event in self.events:
			if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
				for tile in self.tiles:
					if tile.IsOver(pygame.mouse.get_pos()):
						return tile
					
					
					
					
					
					
					
					
					