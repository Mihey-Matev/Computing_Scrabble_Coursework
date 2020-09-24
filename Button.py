import pygame
import VisualObject as VO
import TextBox
	
class Button(VO.VisualObject):
	def __init__(
				self, 
				colour = (255, 255, 255),
				position = (0, 0),
				width = 50, 
				height = 50, 
				outline_colour = None, 
				text='', 
				text_size = 20, 
				text_colour = (0, 0, 0), 
				fade_value = 20,
				is_active = True,
				outline_size = 4):

		super(Button, self).__init__(position)
		self.fade_value = fade_value
		
		self.SetColour(colour)
		if outline_colour is None:
			self.outline_colour = colour
		else:
			self.outline_colour = outline_colour
		#self.text_colour = text_colour
		
		x = self.position[0]
		y = self.position[1]
		
		self.outline_size = outline_size
		
		self.width = width# - self.outline_size
		self.height = height# - self.outline_size
		#self.text = text
		#self.text_size = text_size
		
		#self.onceOver = False		
		
		if text != "":
			font = pygame.font.SysFont('arial', text_size)
			font_text = font.render(text, 1, text_colour)
			
			self.btn_text = TextBox.TextBox(
										(x + (self.width/2 - font_text.get_width()/2), y + (self.height/2 - font_text.get_height()/2)),
										text,
										text_size,
										'arial',
										text_colour
										)
			
		self.is_active = is_active

	def GetSize(self):
		return (self.width, self.height)
	
	
	def ToggleIsActive(self):
		self.is_active = not self.is_active
		if self.is_active:
			self.SetOriginalColour()
		else:
			self.SetUnclickableColour()
		
	def GetIsActive(self):
		return self.is_active
	

	# As I want the button to fade when the mouse is hovering over it, I need to make sure that its colour doesn't go into the negatives and cause and error. This is why i have a specific setter.
	def SetColour(self, colour):
		# Correction for colour if it's outside of the 0 to 255 range when fade values are applied
		colour_list = list(colour)		
		if colour[0] < self.fade_value:
			colour_list[0] = self.fade_value + colour_list[0]
		if colour[1] < self.fade_value:
			colour_list[1] = self.fade_value + colour_list[1]
		if colour[2] < self.fade_value:
			colour_list[2] = self.fade_value + colour_list[2]
			
		if colour[0] + self.fade_value > 255:
			colour_list[0] = 255 - self.fade_value
		if colour[1] + self.fade_value > 255:
			colour_list[1] = 255 - self.fade_value
		if colour[2] + self.fade_value > 255:
			colour_list[2] = 255 - self.fade_value
			
		# In case the above corrections don't work, this makes it so that disabling/hovering over the button doesn't error
		for n in colour:
			if n < 0 or n > 255:
				self.fade_colour = 0
				colour_list = colour
				break
			
		self.colour = tuple(colour_list)
		self.original_colour = self.colour
		
		
	# this method draws the button (by drawing its rectangles and text)
	def Draw(self, surface):
		pygame.draw.rect(surface, self.outline_colour, (self.position[0] - 0.5 * self.outline_size, self.position[1] - 0.5 * self.outline_size,self.width + self.outline_size,self.height + self.outline_size), 0)            
		#print (self.colour)
		pygame.draw.rect(surface, self.colour, (self.position[0], self.position[1],self.width,self.height),0)
        
		if not (self.btn_text is None):
			"""
			btn_text = TextBox.TextBox(
										(self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)),
										self.text,
										self.text_size
										'arial',
										self.text_colour
										)										
			"""
			self.btn_text.Draw(surface)
			#font = pygame.font.SysFont('arial', self.text_size)
			#text = font.render(self.text, 1, self.text_colour)
			#pygame.display.get_surface().blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

	
	def SetUnclickableColour(self):
		self.colour = tuple(map(lambda x: x + self.fade_value, self.original_colour))
	
	def SetHoveringColour(self):
		self.colour = self.colour = tuple(map(lambda x: x - self.fade_value, self.original_colour))
		
	def SetOriginalColour(self):
		self.colour = self.original_colour
			
			
	# The method which checks if the mouse is hovering over the button
	def IsOver(self, pos):
		if self.GetIsActive():
			#Pos is the mouse position or a tuple of (x,y) coordinates		
			if pos[0] > self.position[0] and pos[0] < self.position[0] + self.width:
				if pos[1] > self.position[1] and pos[1] < self.position[1] + self.height:
					#if not self.onceOver:
					self.SetHoveringColour()
						#self.colour = (self.colour[0] - self.fade_value, self.colour[1] - self.fade_value, self.colour[2] - self.fade_value)
						#self.onceOver = True
					return True

			self.SetOriginalColour()
			#if self.onceOver:
			#	self.colour = (self.colour[0] + self.fade_value, self.colour[1] + self.fade_value, self.colour[2] + self.fade_value) 
			#	self.onceOver = False
			return False
	
	
	
	
	
	
	
	
	
	
	
	