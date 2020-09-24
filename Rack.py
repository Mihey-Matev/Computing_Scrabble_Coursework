import pygame
import VisualObject as VO
import Tile
import Button as Btn

class Rack(VO.VisualObject):
	def __init__(self, position = (0, 0), tile_width = 50, tile_height = 50, lettertile_letters = []):		
		super(Rack, self).__init__(position)		
		self.rack_colour = (255, 255, 0)
		
		self.tile_height = tile_height
		self.tile_width = tile_width
		
		self.height = 10 * tile_height
		self.width = tile_width
		self.PopulateRack(lettertile_letters)
		
	def Draw(self, surface):
		pygame.draw.rect(surface, self.rack_colour, (self.position, (self.width, self.height)),0)
		
		for tile in self.lettertiles:
			tile.Draw(surface)
	
	
	def ProcessInput(self, events):
		self.events = events
		return self.GetTileRelativePositionOfCLickedTile()
	
	
	def SetPosition(self, position):
		super(Rack, self).SetPosition(position)
		for y, tile in enumerate(self.lettertiles):
			tile.SetPosition((self.position[0], self.position[1] + y * 1.5 * self.tile_height))
		
	
	
	def PopulateRack(self, lettertile_letters):
		shorter_side_length = min(self.tile_height, self.tile_width)
		PIXEL_TO_POINT_FACTOR = 0.75
		text_size = round(PIXEL_TO_POINT_FACTOR * (shorter_side_length - 12))
		
		self.lettertiles = [Tile.Tile(
									colour = (215, 215, 0),
									position = (self.position[0], self.position[1] + n * 1.5 * (self.tile_height)),
									width = self.tile_width, 
									height = self.tile_height, 
									outline_colour = (100, 100, 0), 
									text = letter, 
									text_size = text_size, 
									text_colour = (0, 0, 0), 
									fade_value = 20,
									is_active = True,
									outline_size = 4)
									for n, letter in enumerate(lettertile_letters)]
	
	
	def FindClickedTile(self):
		for tile in self.lettertiles:
			tile.IsOver(pygame.mouse.get_pos())
		
		for event in self.events:
			if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
				for tile in self.lettertiles:
					if tile.IsOver(pygame.mouse.get_pos()):
						return tile
	
	
	def GetTileRelativePosition(self, tile):
		return self.lettertiles.index(tile)
	
	
	def GetTileRelativePositionOfCLickedTile(self):
		if not (self.FindClickedTile() is None):
			return self.GetTileRelativePosition(self.FindClickedTile())
	
	
	
	
	