import pygame
import Button as Btn

class LetterTileHolder(Btn.Button):
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
				tile = None):
		super(LetterTileHolder, self).__init__(
										colour = colour,
										position = position,
										width = width, 
										height = height, 
										outline_colour = outline_colour, 
										text = text, 
										text_size = text_size, 
										text_colour = text_colour, 
										fade_value = fade_value,
										is_active = is_active,
										outline_size = outline_size)
		self.my_tile = tile
		
		
	def SetPosition(self, pos):
		if self.GetTile() != None:
			self.GetTile().SetPosition(pos)
		super(LetterTileHolder, self).SetPosition(pos)


	def PlaceTile(self, tile):
		old_tile = self.RemoveTile
		self.my_tile = tile
		return old_tile
	
	
	def HasTile(self):
		return (not not self.my_tile)

	
	def Deactivate(self):
		super(LetterTileHolder, self).Deactivate()
		self.my_tile.Deactivate()
	
	
	def MoveTileTo(self, new_holder):
		if self.GetTile() != None and new_holder.GetTile() == None:
			self.GetTile().SetPosition(new_holder.GetPosition())
			new_holder.PlaceTile(self.RemoveTile())
			return True
		else:
			return False
			
			
	def SetPosition(self, position):
		super(LetterTileHolder, self).SetPosition(position)
		if self.my_tile != None: self.my_tile.SetPosition(position)
			
			
	def Draw(self, surface):
		if self.GetTile() != None:
			self.GetTile().Draw(surface)
		else:
			super(LetterTileHolder, self).Draw(surface)


	def RemoveTile(self):
		temp_tile = self.GetTile()
		self.my_tile = None
		return temp_tile


	def IsOver(self, pos):			
		if self.my_tile != None:
			return self.GetTile().IsOver(pos)
		else:
			return super(LetterTileHolder, self).IsOver(pos)


	def GetTile(self):
		return self.my_tile