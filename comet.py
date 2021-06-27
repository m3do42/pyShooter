import pygame
import random

# Comet class
class Comet(pygame.sprite.Sprite):

	def __init__(self, comet_event):
		super().__init__()
		# Define comet image
		self.image = pygame.image.load('assets/comet.png')
		self.rect = self.image.get_rect()
		self.velocity = random.randint(1, 3)
		self.rect.x = random.randint(20, 800)
		self.rect.y = - random.randint(0, 800)
		self.comet_event = comet_event

	def remove(self):
		self.comet_event.all_comets.remove(self)

		# Play sound
		self.comet_event.game.sound_manager.play('meteorite')

		# Check if all comets are delete
		if len(self.comet_event.all_comets) == 0:
			# Re init game bar
			self.comet_event.reset_percent()
			# Add 2 monsters
			self.comet_event.game.start()

	def fall(self):
		self.rect.y += self.velocity

		# Check if the comet is out screen
		if self.rect.y >= 500:
			# Delete comet
			self.remove()
			# Check if all comets are delete
			if len(self.comet_event.all_comets) == 0:
				# Re init
				self.comet_event.reset_percent()
				self.comet_event.fall_mode = False


		if self.comet_event.game.check_collision(self, self.comet_event.game.all_players):
			# Delete comet
			self.remove()
			# Add damage
			self.comet_event.game.player.damage(20)