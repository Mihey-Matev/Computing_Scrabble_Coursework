import pygame
import VisualObject as VO
import GLetterTile
import Button as Btn
import LetterTileHolder

class Rack(VO.VisualObject):
	def __init__(self, position = (0, 0), tile_width = 50, tile_height = 50):#, lettertile_letters = None):		
		super(Rack, self).__init__(position)		
		self.rack_colour = (255, 255, 0)
		
		self.tile_height = tile_height
		self.tile_width = tile_width
		
		self.height = 10 * tile_height
		self.width = tile_width
		
		#if len(lettertile_letter) == 0:
		#	lettertile_letter = [None] * 7
		#self.PopulateRack(lettertile_letters)
		self.SetHolders()
		self.covered = False
		
		
	def CoverRack(self):
		self.covered = True
		
	def UncoverRack(self):
		self.covered = False
		
	def Draw(self, surface):
		pygame.draw.rect(surface, self.rack_colour, (self.position, (self.width, self.height)), 0)
		#print (self.covered)
		if not self.covered:
			for holder in self.holders:
				holder.Draw(surface)
	
	
	def ProcessInput(self, events):
		self.events = events
		return self.GetHolderRelativePositionOfCLickedHolder()
	
	
	def SetPosition(self, position):
		super(Rack, self).SetPosition(position)
		for y, holder in enumerate(self.holders):
			holder.SetPosition((self.position[0], self.position[1] + y * 1.5 * self.tile_height))
		
	
	"""
	def PopulateRack(self):#, lettertiles):
		shorter_side_length = min(self.tile_height, self.tile_width)
		PIXEL_TO_POINT_FACTOR = 0.75
		text_size = round(PIXEL_TO_POINT_FACTOR * (shorter_side_length - 12))
		
		self.lettertiles = [GLetterTile.GLetterTile(
									colour = (215, 215, 0),
									position = (self.position[0], self.position[1] + n * 1.5 * (self.tile_height)),
									width = self.tile_width, 
									height = self.tile_height, 
									outline_colour = (100, 100, 0), 
									text = "",#letter[0], 
									text_size = text_size, 
									text_colour = (0, 0, 0), 
									fade_value = 20,
									is_active = True,
									outline_size = 4,
									point_worth = "")#letter[1])
									for n in range(7)]
									#for n, letter in enumerate(lettertiles)]
									
	"""
	
	def SetHolders(self):
		shorter_side_length = min(self.tile_height, self.tile_width)
		PIXEL_TO_POINT_FACTOR = 0.75
		text_size = round(PIXEL_TO_POINT_FACTOR * (shorter_side_length - 12))
		
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
	
	
	def PopulateRack(self, lettertiles):
		shorter_side_length = min(self.tile_height, self.tile_width)
		text_size = round(0.75 * (shorter_side_length - 12))
		
		for n, tile in enumerate(lettertiles):			
			if tile == None:
				self.holders[n].RemoveTile()
			elif tile[0] != str(self.holders[n].GetTile()) and self.holders[n].GetTile() == None:
				#print (str(self.holders[n].GetTile()))
				#print (tile[0])
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
				#print (tile[1])
			elif self.holders[n].GetTile() != None:
				self.holders[n].GetTile().ChangeLooks(letter = tile[0], point_worth = tile[1])
			
		"""
		self.lettertiles = [GLetterTile.GLetterTile(
									colour = (215, 215, 0),
									position = (self.position[0], self.position[1] + n * 1.5 * (self.tile_height)),
									width = self.tile_width, 
									height = self.tile_height, 
									outline_colour = (100, 100, 0), 
									text = letter[0], 
									text_size = text_size, 
									text_colour = (0, 0, 0), 
									fade_value = 20,
									is_active = True,
									outline_size = 4,
									point_worth = letter[1])
									#for n in range(7)]
									for n, letter in enumerate(lettertiles)]
		
		"""
	"""
	# this function takes in the lettertiles (their letter and point worth) and graphically changes the lettertiles on the rack to look to match them
	def SetTileRackGLetterTileAttributes(self, new_lettertiles):
		new_lettertiles_copy = new_lettertiles[:] + (7 - len(new_lettertiles)) * [("", "")]
		for lettertile in enumerate(self.lettertiles):
			lettertile.ChangeLooks(letter = new_lettertiles[0], point_worth = new_lettertiles[1])
	"""
	
	
	# finds the holder which was clicked in the last frame
	def FindClickedHolder(self):
		for holder in self.holders:
			holder.IsOver(pygame.mouse.get_pos())
		
		for event in self.events:
			if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
				for holder in self.holders:
					if holder.IsOver(pygame.mouse.get_pos()):# and holder.GetText() != "":
						return holder
	
	# gets the position in the rack of a certain holder
	def GetHolderRelativePosition(self, holder):
		return self.holders.index(holder)
	
	
	# gets the position in the rack of the clicked holder
	def GetHolderRelativePositionOfCLickedHolder(self):
		if not (self.FindClickedHolder() is None):
			holder = self.FindClickedHolder()
			return (holder, self.GetHolderRelativePosition(holder))
		
		
	def GetTileLetter(self):
		if self.my_tile != None:
			return str(self.my_tile)
	
	
	
	
	