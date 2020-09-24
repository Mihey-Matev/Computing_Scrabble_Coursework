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
		

	# If i want to put a GLetterTIle in this holder, it needs to be done throguh this method.
	def PlaceTile(self, tile):
		old_tile = self.RemoveTile()
		self.my_tile = tile
		self.my_tile.SetPosition(self.position)
		return old_tile	
	
	# returns boolean for whether there is a GLetterTile seated in this object
	def HasTile(self):
		return (not not self.my_tile)
	
	# Because both the tile in the holder and the holder itself could potentially be interacted with, I disable both to make sure there is no chance of them being interacted with once Deactivated().
	def Deactivate(self):
		super(LetterTileHolder, self).Deactivate()
		self.my_tile.Deactivate()	
	
	# Allows me to easily move a GLetterTile between two holders
	def MoveTileTo(self, new_holder):
		if self.GetTile() != None and new_holder.GetTile() == None:
			self.GetTile().SetPosition(new_holder.GetPosition())
			new_holder.PlaceTile(self.RemoveTile())
			return True
		else:
			return False			
		
	# positions of elements it contains need to be changed as well
	def SetPosition(self, position):
		super(LetterTileHolder, self).SetPosition(position)
		if self.my_tile != None: self.my_tile.SetPosition(position)			
			
	def Draw(self, surface):
		if self.GetTile() != None:
			self.GetTile().Draw(surface)
		else:
			super(LetterTileHolder, self).Draw(surface)

	# If i want to remove the tile which is currently in this holder, it needs to be donw throguh this
	def RemoveTile(self):
		temp_tile = self.GetTile()
		self.my_tile = None
		return temp_tile

	# this is an alteration to the Button's IsOver() method. Mainly used so the user knows if they are hovering over the holder (by showing it on the GLetterTile it contains if it contains one)
	def IsOver(self, pos):			
		if self.my_tile != None:
			return self.GetTile().IsOver(pos)
		else:
			return super(LetterTileHolder, self).IsOver(pos)

	# gets the GLetterTile of this holder
	def GetTile(self):
		return self.my_tile
	