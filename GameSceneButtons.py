import pygame
import VisualObject as VO
import Button as Btn

class GameSceneButtons(VO.VisualObject):
	def __init__(self, position = (0, 0), button_width = 150, button_height = 50):
		super(GameSceneButtons, self).__init__(position)		
		self.colour = (0, 100, 255)
		self.button_width = button_width
		self.button_height = button_height
		self.height = button_height * 7
		self.width = button_width
		
		self.tile_bag_btn = Btn.Button(colour = (self.colour[0], 0, self.colour[2] - 30), position = self.position, width = self.button_width, height = self.button_height, outline_colour = (self.colour[0], 0, self.colour[2] - 110), text = "Tile Bag", text_size = round(self.button_height * 0.4), text_colour = (255, 255, 255), fade_value = 20, is_active = True, outline_size = 6)
		self.pass_turn_btn = Btn.Button(colour = (self.colour[0], 0, self.colour[2] - 30), position = (self.position[0], self.position[1] + 1.5 * self.button_height), width = self.button_width, height = self.button_height, outline_colour = (self.colour[0], 0, self.colour[2] - 110), text = "Pass Turn", text_size = round(self.button_height * 0.4), text_colour = (255, 255, 255), fade_value = 20, is_active = True, outline_size = 6)
		self.swap_tiles_btn = Btn.Button(colour = (self.colour[0], 0, self.colour[2] - 30), position = (self.position[0], self.position[1] + 3 * self.button_height), width = self.button_width, height = self.button_height, outline_colour = (self.colour[0], 0, self.colour[2] - 110), text = "Swap Tiles", text_size = round(self.button_height * 0.4), text_colour = (255, 255, 255), fade_value = 20, is_active = True, outline_size = 6)
		self.shuffle_tiles_btn = Btn.Button(colour = (self.colour[0], 0, self.colour[2] - 30), position = (self.position[0], self.position[1] + 4.5 * self.button_height), width = self.button_width, height = self.button_height, outline_colour = (self.colour[0], 0, self.colour[2] - 110), text = "Shuffle Tiles", text_size = round(self.button_height * 0.4), text_colour = (255, 255, 255), fade_value = 20, is_active = True, outline_size = 6)
		self.resign_btn = Btn.Button(colour = (self.colour[0], 0, self.colour[2] - 30), position = (self.position[0], self.position[1] + 6 * self.button_height), width = self.button_width, height = self.button_height, outline_colour = (self.colour[0], 0, self.colour[2] - 110), text = "Resign", text_size = round(self.button_height * 0.4), text_colour = (255, 255, 255), fade_value = 20, is_active = True, outline_size = 6)
		
		self.buttons_list = [self.tile_bag_btn, self.pass_turn_btn, self.swap_tiles_btn, self.shuffle_tiles_btn, self.resign_btn]
		
	# returns an integer between 0 and 4, each corresponding to a different button clicked; 0 - tile_bag_btn, 1 - pass_turn_btn, 2 - swap_tiles_btn, 3 - shuffle_tiles_btn, 4 - resign_btn
	# the GameScene is expected to know how to deal with this
	def ProcessInput(self, events):
		self.events = events
		if not (self.FindClickedBtn() is None):
			return self.buttons_list.index(self.FindClickedBtn())
	
	
	def GetSize(self):
		return (self.width, self.height)
			
	def FindClickedBtn(self):
		for btn in self.buttons_list:
			btn.IsOver(pygame.mouse.get_pos())
		
		for event in self.events:
			if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
				for btn in self.buttons_list:
					if btn.IsOver(pygame.mouse.get_pos()):
						return btn
					
					
	def SetPosition(self, position):
		super(GameSceneButtons, self).SetPosition(position)
		for y, tile in enumerate(self.buttons_list):
			tile.SetPosition((self.position[0], self.position[1] + y * 1.5 * self.button_height))
					
				
	def Draw(self, surface):
		pygame.draw.rect(surface, self.colour, (self.position, (self.width, self.height)),0)
		
		for tile in self.buttons_list:
			tile.Draw(surface)