# This class doesn't work
# why is it here?

# i wrote this based off several StackOverflow posts and videos on YouTube, but this doesn't work (it runs but no errors)

# i just manually wrote the functions in the live loop instead, much dirtier and sillier, but at least it works

import pygame, WorldGen

class CameraGroup(pygame.sprite.Group):
	def __init__(self):
		super().__init__()
		
		self.list = CameraGroup.sprites(self)
	

	def moveRight(self):
		print("Right")
		for sprite in self.list:
			print(sprite)
			sprite.rect.x -=100

	def moveUp(self):
		print("Up")
		for sprite in self.list:
			print(self.list)
			sprite.rect.y +=100

	def moveDown(self):
		print("Down")
		for sprite in self.list:
			sprite.rect.y -=100

	def moveLeft(self):
		print("Left")
		for sprite in self.list:
			print(self.list)
			sprite.rect.x +=100
