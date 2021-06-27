import pygame
import random
import animation

# Monster class
class Monster(animation.AnimateSprite):

	def __init__(self, game, name, size, offset=0):
		super().__init__(name, size)
		self.game = game
		self.health = 100
		self.max_health = 100
		self.attack = 0.3
		self.rect = self.image.get_rect()
		self.rect.x = 1000 + random.randint(0, 300)
		self.rect.y = 540 - offset
		self.loot_amount = 10
		self.start_animation()

	def set_speed(self, speed):
		self.default_speed = speed
		self.velocity = random.randint(1, 3)

	def set_loot_amount(self, amount):
		self.loot_amount = amount

	def damage(self, amount):
		# Inflict damage
		self.health -= amount

		# Check if the monster is dead
		if self.health <= 0:
			# Redefine monster
			self.rect.x = 1000 + random.randint(0, 300)
			self.velocity = random.randint(1, self.default_speed)
			self.health = self.max_health

			# Add player point
			self.game.add_score(self.loot_amount)

		# Check is load bar is full
		if self.game.comet_event.is_full_loaded():
			# Delete monsters
			self.game.all_monsters.remove(self)

			# Call method for comets
			self.game.comet_event.attempt_fall()

	def update_animation(self):
		self.animate(loop=True)

	def update_health_bar(self, surface):
		# Draw health bar
		pygame.draw.rect(surface, (60,63,60), [self.rect.x + 10, self.rect.y - 20, self.max_health, 5])
		pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 10, self.rect.y - 20, self.health, 5])

	def forward(self):
		# Check if monsters is not in collision with player (group) 
		if not self.game.check_collision(self, self.game.all_players):
			self.rect.x -= self.velocity
		# If the monster is in collision with the player
		else:
			# Inflict damage
			self.game.player.damage(self.attack)


# Mummy class
class Mummy(Monster):

	def __init__(self, game):
		super().__init__(game, "mummy", (130, 130))
		self.set_speed(3)
		self.set_loot_amount(20)

# Alien class
class Alien(Monster):

	def __init__(self, game):
		super().__init__(game, "alien", (300, 300), 130)
		self.health = 250
		self.max_health = 250
		self.attack = 0.8
		self.set_speed(1)
		self.set_loot_amount(50)