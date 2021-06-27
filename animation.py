import pygame

# Animation class
class AnimateSprite(pygame.sprite.Sprite):

	# Define move for entity
	def __init__(self, sprite_name, size=(200, 200)):
		super().__init__()
		self.size = size
		self.image = pygame.image.load(f'assets/{sprite_name}.png')
		self.image = pygame.transform.scale(self.image, size)
		self.current_image = 0 # Begin by first image
		self.images = animations.get(sprite_name)
		self.animation = False

	# Start animation
	def start_animation(self):
		self.animation = True

	# Define method for sprite animation
	def animate(self, loop=False):
		# Check is animation is activate
		if self.animation:
			# Load next sprite
			self.current_image += 1

			# Check if animation is finish
			if self.current_image >= len(self.images):
				# Re init animation
				self.current_image = 0

				# Check if animation is a loop
				if loop is False:
					# Disable animation
					self.animation = False

			# Update sprite
			self.image = self.images[self.current_image]
			self.image = pygame.transform.scale(self.image, self.size)

# Load all sprites animation
def load_animation_images(sprite_name):
	images = []

	# Get folder path
	path = f"assets/{sprite_name}/{sprite_name}"

	# Animation loop
	for num in range(1, 24):
		image_path = path + str(num) + '.png'
		images.append(pygame.image.load(image_path))

	# Return sprites list
	return images

# Define dictionary for load pictures
# mummy -> [...mummy1.png, ...mummy.png, ...]
# player -> [...player1.png, ...player.png, ...]
# alien -> [...alien.png, ...alien.png, ...]
animations = {
	'mummy': load_animation_images('mummy'),
	'player': load_animation_images('player'),
	'alien': load_animation_images('alien')
}