import pygame
import VisualObject as VO
import GLetterTile
import Button as Btn
import LetterTileHolder

class Rack(VO.VisualObject):
	def __init__(self, position = (0, 0), tile_width = 50, tile_height = 50):
		super(Rack, self).__init__(position)		
		self.rack_colour = (255, 255, 0)
		
		self.tile_height = tile_height
		self.tile_width = tile_width
		
		self.height = 10 * tile_height
		self.width = tile_width
		
		self.SetHolders()
		self.covered = False
				
	# The following two methods are used when two players are playing locally (on one computer) and they need to switch. It hides the current player's rack, giving time for the players to swap and not get any extra information.
	def CoverRack(self):
		self.covered = True
		
	def UncoverRack(self):
		self.covered = False
		
	def Draw(self, surface):
		pygame.draw.rect(surface, self.rack_colour, (self.position, (self.width, self.height)), 0)
		if not self.covered:
			for holder in self.holders:
				holder.Draw(surface)
		
	def ProcessInput(self, events):
		self.events = events
		return self.GetHolderRelativePositionOfCLickedHolder()
		
	# we have to change the position of this element and the ones it contains (i.e. the tileholders), so we have to edit the parent's method.
	def SetPosition(self, position):
		super(Rack, self).SetPosition(position)
		for y, holder in enumerate(self.holders):
			holder.SetPosition((self.position[0], self.position[1] + y * 1.5 * self.tile_height))
			
	# calculates the position for and instantiates the letterholders
	def SetHolders(self):
		shorter_side_length = min(self.tile_height, self.tile_width)
		text_size = round(0.49 * (shorter_side_length))
		
		self.holders = [LetterTileHolder.LetterTileHolder(
									colour = (190, 190, 0),
									position = (self.position[0], self.position[1] + n * 1.5 * (self.tile_height)),
									width = self.tile_width, 
									height = self.tile_height, 
									outline_colour = (100, 100, 0), 
									text = "",
									text_size = text_size, 
									text_colour = (0, 0, 0), 
									fade_value = 20,
									is_active = True,
									outline_size = 4
									)
									for n in range(7)]
		
	# Fills out the visual rack with the tiles of the logical rack (of the current player, but only receives a list as an argument, so this has to be specified on passing)
	def PopulateRack(self, lettertiles):
		shorter_side_length = min(self.tile_height, self.tile_width)
		text_size = round(0.49 * (shorter_side_length))
		
		for n, tile in enumerate(lettertiles):			
			if tile == None:		# if the player's rack contains nothing in this position, remove any tile thaat was in this position on the visual rack
				self.holders[n].RemoveTile()
			elif tile[0] != str(self.holders[n].GetTile()) and self.holders[n].GetTile() == None:	# if there is a tile in this position of the player's rack, but there is no visual tile currently in this position of the rack, then create a new tile here
				self.holders[n].PlaceTile(GLetterTile.GLetterTile(
										colour = (215, 215, 0),
										position = self.holders[n].GetPosition(),
										width = self.holders[n].GetSize()[0], 
										height = self.holders[n].GetSize()[1], 
										outline_colour = (100, 100, 0), 
										text = tile[0], 
										text_size = text_size, 
										text_colour = (0, 0, 0), 
										fade_value = 30,
										is_active = True,
										outline_size = 4,
										point_worth = tile[1])
										)
			elif self.holders[n].GetTile() != None:		# if there is a tile in this position but its letter is different, then change the letter of the tile which is in this location
				self.holders[n].GetTile().ChangeLooks(letter = tile[0], point_worth = tile[1])
		
	# finds the holder which was clicked in the last frame
	def FindClickedHolder(self):
		for holder in self.holders:
			holder.IsOver(pygame.mouse.get_pos())
		
		for event in self.events:
			if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
				for holder in self.holders:
					if holder.IsOver(pygame.mouse.get_pos()):
						return holder
	
	# gets the position in the rack of a certain holder
	def GetHolderRelativePosition(self, holder):
		return self.holders.index(holder)	
	
	# gets the position in the rack of the clicked holder
	def GetHolderRelativePositionOfCLickedHolder(self):
		if not (self.FindClickedHolder() is None):
			holder = self.FindClickedHolder()
			return (holder, self.GetHolderRelativePosition(holder))		
	
	
	