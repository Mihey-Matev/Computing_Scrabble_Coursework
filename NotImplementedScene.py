import Scene
import TextBox

class NotImplementedScene(Scene.Scene):
	def __init__(self, width, height):
		super(NotImplementedScene, self).__init__(width, height)
		
		# Create text to tell the user what is going on
		self.warning_text_part1 = self.AddText((0, 0), "Sorry, this part of the game", int(self.surface.get_width() / 16))
		self.CentreVOOnPos(self.warning_text_part1, (self.GetCentreCoordinates()[0], self.GetCentreCoordinates()[1] - self.warning_text_part1.GetSize()[1] * 1.1))
		
		self.warning_text_part2 = self.AddText((0, 0), "has not been implemented yet.", int(self.surface.get_width() / 16))
		self.CentreVOOnPos(self.warning_text_part2)
		
		self.warning_text_part3 = self.AddText((0, 0), "Please come back later.", int(self.surface.get_width() / 16))
		self.CentreVOOnPos(self.warning_text_part3, (self.GetCentreCoordinates()[0], self.GetCentreCoordinates()[1] + self.warning_text_part3.GetSize()[1] * 1.1))
		
	def ProcessInput(self, events):
		pass

	def Update(self):
		pass