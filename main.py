import pygame
import math
from game import Game
from sounds import SoundManager

pygame.init()

# Define a clock (FPS)
clock = pygame.time.Clock()
FPS = 60

# Init app window
pygame.display.set_caption("pyShooter")
# pygame.display.set_caption("Shooter", [Icon path])

screen = pygame.display.set_mode((1080, 720))

# Load background picture
background = pygame.image.load('assets/bg.jpg')

# Load banner
banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)

# Load Start button
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33)
play_button_rect.y = math.ceil(screen.get_height() / 2)

# Load Game
game = Game()

running = True

# Game boucle
while running:

	# Add background on screen
	screen.blit(background, (0, -200))

	# Check if the game is started or not
	if game.is_playing:
		# Launch play instructions
		game.update(screen)
	else:
		# Add home
		screen.blit(play_button, play_button_rect)
		screen.blit(banner, banner_rect)
		
	# Refresh screen
	pygame.display.flip()

	# If the player close windows
	for event in pygame.event.get():
		# Get close window event
		if event.type == pygame.QUIT:
			running = False
			pygame.quit()

		# Detect keydown
		elif event.type == pygame.KEYDOWN:
			game.pressed[event.key] = True

			# Detect space key for projectiles
			if event.key == pygame.K_SPACE:
				if game.is_playing:
					game.player.launch_projectile()
				else:
					# Get play game
					game.start()

					# Play sound
					game.sound_manager.play('click')

		# Detect keyup
		elif event.type == pygame.KEYUP:
			game.pressed[event.key] = False

		#
		elif event.type == pygame.MOUSEBUTTONDOWN:
			# Check if mouse is in collision with the play button
			if play_button_rect.collidepoint(event.pos):
				# Get play game
				game.start()

				# Play sound
				game.sound_manager.play('click')

	# Set FPS
	clock.tick(FPS)