import pygame
from comet import Comet

# Comet Event class
class CometFallEvent:

	# Loading -> Create count
	def __init__(self, game):
		self.percent = 0
		self.percent_speed = 5
		self.game = game
		self.fall_mode = False

		# Define sprite group for comets
		self.all_comets = pygame.sprite.Group()

	def add_percent(self):
		self.percent += self.percent_speed / 100

	def is_full_loaded(self):
		return self.percent >= 100

	def reset_percent(self):
		self.percent = 0

	def meteor_fall(self):
		for i in range(1, 10):
			# Add comets
			self.all_comets.add(Comet(self))

	def attempt_fall(self):
		# Check if load bar is full
		if self.is_full_loaded() and len(self.game.all_monsters) == 0:
			self.meteor_fall()
			self.fall_mode = True # Activate comet event

	def update_bar(self, surface):
		# Add percent to bar
		self.add_percent()

		# Background bar (black)
		pygame.draw.rect(surface, (0, 0, 0), [
			0, # X axis
			surface.get_height() - 20, # Y axis
			surface.get_width(), # Window length
			10 # Bar thickness
		])

		# Bar (red)
		pygame.draw.rect(surface, (187, 11, 11), [
			0, #  X axis
			surface.get_height() - 20, # Y axis
			(surface.get_width() / 100) * self.percent, # Window length
			10 # Bar thickness
		])	