from player import Player
from monster import Monster
from monster import Mummy
from monster import Alien
from comet_event import CometFallEvent
import pygame

from sounds import SoundManager

# Game class
class Game:

	def __init__(self):
		# Define if the game is started
		self.is_playing = False

		# Player generate
		self.all_players = pygame.sprite.Group()
		self.player = Player(self)
		self.all_players.add(self.player)

		# Event generate
		self.comet_event = CometFallEvent(self)

		# Monsters
		self.all_monsters = pygame.sprite.Group()

		# Sound manager
		self.sound_manager = SoundManager()

		# Add font
		self.font = pygame.font.Font("assets/font/PottaOne-Regular.ttf", 25)

		# Init score
		self.score = 0

		self.pressed = {}

	def start(self):
		self.is_playing = True
		self.spawn_monster(Mummy)
		self.spawn_monster(Mummy)
		self.spawn_monster(Alien)

	def add_score(self, points=10):
		self.score += points

	def game_over(self):
		# Re-Init game
		self.all_monsters = pygame.sprite.Group()
		self.comet_event.all_comets = pygame.sprite.Group()
		self.player.health = self.player.max_health
		self.comet_event.reset_percent()
		self.is_playing = False
		self.score = 0

		# Play sound
		game.sound_manager.play('game_over')

	def update(self, screen):
		# Display score
		score_text = self.font.render(f"Score : {self.score}", 1, (0, 0, 0))
		screen.blit(score_text, (20, 20))

		# Add player on screen
		screen.blit(self.player.image, self.player.rect)

		# Refresh player health bar
		self.player.update_health_bar(screen)

		# Refresh game event bar
		self.comet_event.update_bar(screen)

		# Get player animation
		self.player.update_animation()
		
		# Get player projectiles
		for projectile in self.player.all_projectiles:
			projectile.move()

		# Get monsters
		for monster in self.all_monsters:
			monster.forward()
			monster.update_health_bar(screen)
			monster.update_animation()

		for comet in self.comet_event.all_comets:
			comet.fall()

		# Add all projectiles
		self.player.all_projectiles.draw(screen)

		# Add all monsters
		self.all_monsters.draw(screen)

		# Add all comets
		self.comet_event.all_comets.draw(screen)

		# Check player mouve
		if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
			self.player.move_right()
		elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
			self.player.move_left()

	def check_collision(self, sprite, group):
		return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

	def spawn_monster(self, monster_class_name):
		self.all_monsters.add(monster_class_name.__call__(self))