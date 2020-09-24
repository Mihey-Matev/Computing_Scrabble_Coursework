import pygame

# Absreact class allowing me to control how the drawing of any class which has a visual part to it is done
class VisualObject:
	def __init__(self, position):#, width = 50, height = 50):
		self.position = position
		#self.surface = pygame.Surface((width, height))
		
	def Draw(self, surface):
		raise NotImplementedError("ProcessInput abstract method must be defined in subclass.")

	def SetPosition(self, position):
		self.position = position
		
	def GetPosition(self):
		return self.position
	
	def GetSize(self):
		raise NotImplementedError("ProcessInput abstract method must be defined in subclass.")