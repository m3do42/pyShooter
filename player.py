import pygame
from projectile import Projectile
import animation

# Player class
class Player(animation.AnimateSprite):

	def __init__(self, game):
		super().__init__('player') # Load super classe pygame sprite
		self.game = game
		self.health = 100
		self.max_health = 100
		self.attack = 10
		self.velocity = 5
		self.all_projectiles = pygame.sprite.Group()
		self.rect = self.image.get_rect()
		self.rect.x = 400
		self.rect.y = 500

	def damage(self, amount):
		# Check is player can be have a damage without dead
		if self.health - amount > amount:
			# Inflict damage
			self.health -= amount
		else:
			# Game Over
			self.game.game_over()

	def update_animation(self):
		self.animate()

	def update_health_bar(self, surface):
		# Draw health bar
		pygame.draw.rect(surface, (60,63,60), [self.rect.x + 50, self.rect.y + 20, self.max_health, 7])
		pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 50, self.rect.y + 20, self.health, 7])

	def launch_projectile(self):
		# Create new projectile
		self.all_projectiles.add(Projectile(self))

		# Start player animation
		self.start_animation()

		# Play sound
		self.game.sound_manager.play('tir')

	def move_right(self):
		# Check if the player is in collision with monsters
		if not self.game.check_collision(self, self.game.all_monsters):
			self.rect.x += self.velocity

	def move_left(self):
		self.rect.x -= self.velocity