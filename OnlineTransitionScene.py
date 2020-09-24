import pygame
import Scene
import Button as Btn

class OnlineTransitionScene(Scene.Scene):
	def __init__(self, director, width, height):
		super(OnlineTransitionScene, self).__init__(director, width, height)
	
	def ProcessInput(self, events):
		"""Called when a specific event is detected in the loop."""
		raise NotImplementedError("ProcessInput abstract method must be defined in subclass.")

	def Update(self):
		"""Called when a specific event is detected in the loop."""
		raise NotImplementedError("ProcessInput abstract method must be defined in subclass.")
	
	def Draw(self):
		"""called when you want to draw the screen."""
		raise NotImplementedError("OnDraw abstract method must be defined in subclass.")