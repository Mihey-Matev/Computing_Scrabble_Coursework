import pygame
	
class Button:
	def __init__(self, colour, x, y, width, height, outline_colour = None, text='', textSize = 20, text_colour = (0, 0, 0)):
		self.fade_value = 20
		self.SetColour(colour)
		if outline_colour is None:
			self.outline_colour = colour
		else:
			self.outline_colour = outline_colour
		self.text_colour = text_colour
		#self.outline = outline
		self.x = x
		self.y = y
		
		self.outline_size = 4
		
		self.width = width - self.outline_size
		self.height = height - self.outline_size
		self.text = text
		self.textSize = textSize
		
		
		
		
		#self.Draw(screen)

	# As I want the button to fade when the mouse is hovering over it, I need to make sure that its colour doesn't go into the negatives and cause and error. This is why i have a specific setter.
	def SetColour(self, colour):
		colour_list = list(colour)		
		if colour[0] < self.fade_value:
			colour_list[0] = self.fade_value + colour_list[0]
		if colour[1] < self.fade_value:
			colour_list[1] = self.fade_value + colour_list[1]
		if colour[2] < self.fade_value:
			colour_list[2] = self.fade_value + colour_list[2]
			
		self.colour = tuple(colour_list)
		
		
	# this method draws the button (by drawing its rectangles and text)
	def Draw(self):#, screen):
		#if outline_colour:
		pygame.draw.rect(pygame.display.get_surface(), self.outline_colour, (self.x - 0.5 * self.outline_size,self.y - 0.5 * self.outline_size,self.width + self.outline_size,self.height + self.outline_size),0)
            
		pygame.draw.rect(pygame.display.get_surface(), self.colour, (self.x,self.y,self.width,self.height),0)
        
		if self.text != '':
			font = pygame.font.SysFont('arial', self.textSize)
			text = font.render(self.text, 1, self.text_colour)
			pygame.display.get_surface().blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

	# The method which checks if the mouse is hovering over the button
	def IsOver(self, pos):
		#Pos is the mouse position or a tuple of (x,y) coordinates
		onceOver = 0
		if pos[0] > self.x and pos[0] < self.x + self.width:
			if pos[1] > self.y and pos[1] < self.y + self.height:
				if not onceOver:
					print ("hi")
					self.colour = (self.colour[0] - self.fade_value, self.colour[1] - self.fade_value, self.colour[2] - self.fade_value)
					onceOver = 1
				return True
			
		if onceOver:
			self.colour = (self.colour[0] + self.fade_value, self.colour[1] + self.fade_value, self.colour[2] + self.fade_value) 
			onceOver = 0
		return False
	
	""""
	def IsClicked(self, pos):
		if event.type == pygame.MOUSEBUTTONDOWN and self.IsOver(pos):
			return True
	"""
	
	
		
	
class Tile(Button):
	def __init__(self):
		print ("Not finished!")


class BoardTile(Tile):
	def __init__(self):
		print ("Not finished!")

		
class LetterTile(Tile):
	def __init__(self):
		print ("Not finished!")	
	

	
	
	
# abandoned classes	
"""
class VisualObj(pygame.sprite.Sprite):
	def __init__(self):
		print ("Not finished!")
	def render(self):
		#pygame method that shows this object
		print ("Not finished!")
"""
"""
class Button(VisualObj):
	def __init__(self):
		print ("Not finished!")
"""
"""
class VSAIBtn(Button):
	def __init__(self):
		print ("Not finished!")
		
class VSPlayerBtn(Button):
	def __init__(self):
		print ("Not finished!")
	
class OnlineBtn(Button):
	def __init__(self):
		print ("Not finished!")
		
class ExitGameBtn(Button):
	def __init__(self):
		print ("Not finished!")
		
class SubmitWordBtn(Button):
	def __init__(self):
		print ("Not finished!")
		
class TileBagBtn(Button):
	def __init__(self):
		print ("Not finished!")
		
class PassBturnBtn(Button):
	def __init__(self):
		print ("Not finished!")
		
class SwapTilesBtn(Button):
	def __init__(self):
		print ("Not finished!")
		
class ShuffleTilesBtn(Button):
	def __init__(self):
		print ("Not finished!")
		
class ResignBtn(Button):
	def __init__(self):
		print ("Not finished!")
"""		
		


		