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
				outline_size = 4):
		super(LetterTileHolder).__init__(
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
										outline_size = 4)