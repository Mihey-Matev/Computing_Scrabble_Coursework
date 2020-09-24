import pygame
import Scene
import Button as Btn
import pygame_textinput as TI

class GetUsernameScene(Scene.Scene):
	def __init__(self, width, height):
		super(GetUsernameScene, self).__init__(width, height)		
		
		# player's name text entry field
		self.username_entry_field = TI.TextInput(font_size = int(width * (13 / 320)), max_text_length = 12)
		self.AddVONonBtn(self.username_entry_field, self.GetCentreCoordinates())
		
		self.explain_text1 = self.AddText((0, 0), "Please enter your nickname:", int(self.surface.get_width() / 16))
		self.CentreVOOnPos(self.explain_text1, (self.GetCentreCoordinates()[0], self.GetCentreCoordinates()[1] - self.explain_text1.GetSize()[1] * 1.3))
		
		self.explain_text2 = self.AddText((0, 0), "Then press enter.", int(self.surface.get_width() / 16))
		self.CentreVOOnPos(self.explain_text2, (self.GetCentreCoordinates()[0], self.GetCentreCoordinates()[1] + self.explain_text2.GetSize()[1] * 1.3))

	def ProcessInput(self, events):		
		if self.username_entry_field.update(events):
			return self.username_entry_field.get_text()

	def Update(self):
		self.CentreVOOnPos(self.username_entry_field)