import pygame
import Button as Btn
import VisualObject as VO
import GLetterTile
import TextBox

class TileBagPopUp(VO.VisualObject):
	def __init__(self, width, height, position, tile_width = 50, tile_height = 50, picker_colour = (217, 160, 107)):
		super(TileBagPopUp, self).__init__(position)
		self.tile_height = tile_height
		self.tile_width = tile_width
		self.width = width
		self.height = height
		self.picker_colour = picker_colour
		self.instruction_text = TextBox.TextBox(
												position = (0, 0),
												text = "These are the tiles left:",
												font_size = int(tile_width * 0.8),
												font_family = "arial",
												text_colour = (0, 0, 0)
												)
		self.instruction_text.SetPosition((self.position[0] + 0.5 * self.width - 0.5 * self.instruction_text.GetSize()[0], self.position[1] + 0.5 * self.instruction_text.GetSize()[1]))
		
		characters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ*")
		self.tiles = {characters[n]:GLetterTile.GLetterTile(
											colour = (210, 210, 0),
											position = (self.position[0] + 0.5 * self.tile_width + (n % 10) * 1.5 * (self.tile_width), self.position[1] + self.tile_height * 2 + int(n / 10) * self.tile_height * 1.8),
											width = self.tile_width, 
											height = self.tile_height, 
											outline_colour = (100, 100, 0), 
											text = characters[n],
											text_size = round(0.75 * (self.tile_width - 12)), 
											text_colour = (0, 0, 0), 
											fade_value = 20,
											is_active = False,
											outline_size = 4,
											point_worth = ""
											)
											for n in range(27)}
		
		self.numbers_of_tiles = {characters[n]:TextBox.TextBox(
												position = (self.position[0] + 0.6 * self.tile_width + (n % 10) * 1.5 * (self.tile_width), self.position[1] + self.tile_height * 3 + int(n / 10) * self.tile_height * 1.8),
												text = "0", 
												font_size = int(self.tile_width * 0.562), 
												font_family = "arial", 
												text_colour = (0, 0, 0))
								 for n in range(27)}
		
		self.exit_btn = Btn.Button(
									colour = (137, 80, 27),
									position = (self.position[0] + self.width - self.tile_width * 0.85, self.position[1] + self.tile_height * 0.25),
									width = self.tile_width * 0.6, 
									height = self.tile_width * 0.6, 
									outline_colour = (237, 180, 127), 
									text = "X", 
									text_size = int(self.tile_width * 0.37), 
									text_colour = (237, 180, 127), 
									fade_value = 20,
									is_active = True,
									outline_size = 4)		
	
	def Draw(self, surface):		
		pygame.draw.rect(surface, self.picker_colour, (self.position, (self.width, self.height)), 0)
		self.instruction_text.Draw(surface)	
		self.exit_btn.Draw(surface)
		for letter, tile in self.tiles.items():
			tile.Draw(surface)
		for letter, num in self.numbers_of_tiles.items():
			num.Draw(surface)
	
	# returns the letter which was clicked
	def ProcessInput(self, events, tiles_amounts):
		self.events = events
		for letter, amount in tiles_amounts.items():
			self.numbers_of_tiles[letter].SetText(amount)
		#for letter, tile in self.tiles.items():
		#	self.numbers_of_tiles[letter].SetText(tiles_amounts[letter])
		
		# If the player presses on the 'x' button, then the object returns true, which can be handled appropriately (to end the event)
		self.exit_btn.IsOver(pygame.mouse.get_pos())
		for event in events:
			if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
				if self.exit_btn.IsOver(pygame.mouse.get_pos()):
					return True	
	
	def SetPosition(self, position):
		for letter, tile in self.tiles.items():
			tile.SetPosition((tile.GetPosition()[0] + position[0] - self.position[0], tile.GetPosition()[1] + position[1] - self.position[1]))
		for letter, num in self.numbers_of_tiles.items():
			num.SetPosition((num.GetPosition()[0] + position[0] - self.position[0], num.GetPosition()[1] + position[1] - self.position[1]))
		self.instruction_text.SetPosition((self.instruction_text.GetPosition()[0] + position[0] - self.position[0], self.instruction_text.GetPosition()[1] + position[1] - self.position[1]))
		self.exit_btn.SetPosition((self.exit_btn.GetPosition()[0] + position[0] - self.position[0], self.exit_btn.GetPosition()[1] + position[1] - self.position[1]))
		super(TileBagPopUp, self).SetPosition(position)
		
		