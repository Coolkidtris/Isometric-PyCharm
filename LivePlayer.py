# This file is just used to render the game
import pygame, sys, WorldGen, ImageHandler, CameraHandler, UiAndGamePlay
from pygame.locals import *

display = pygame.Surface((300, 300), pygame.SRCALPHA)
clock = pygame.time.Clock()

# zoom variables
zoomAmnt = 1 # amount to zoom by, wil cap at 5 and -5 as maximum zoom values
# world rendering
def renderWorld(PlayerWorld):
	global zoomAmnt
	pygame.init()
	screen = pygame.display.set_mode((650, 650),0,32)
	pygame.display.set_caption(f'{PlayerWorld} City')
	WorldGen.drawMap(display, PlayerWorld, ImageHandler.Sprites)
	
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN: 
				if event.key == pygame.K_ESCAPE:
					pygame.quit()
					sys.exit()

		Keys = pygame.key.get_pressed() # get a state for all the keys pressed

		if Keys[pygame.K_a]:
			for sprite in WorldGen.cameraSprites.sprites(): # move the sprites while the key is pressed
				sprite.rect.x += 3
		if Keys[pygame.K_d]:
			for sprite in WorldGen.cameraSprites.sprites():
				sprite.rect.x -= 3
		if Keys[pygame.K_w]:
			for sprite in WorldGen.cameraSprites.sprites():
				sprite.rect.y += 3
		if Keys[pygame.K_s]:
			for sprite in WorldGen.cameraSprites.sprites():
				sprite.rect.y -= 3

######## Zooming does NOT work. or, kinda. its  very broken. unindent at your own risk ##############

		if Keys[pygame.K_q]: # if zoom keys such as Q or E are being pressed
			for sprite in WorldGen.cameraSprites.sprites():
				zoomAmnt-=0.1
				sprite.rect.x = sprite.rect.x * 1.1
				sprite.rect.y = sprite.rect.y * 1.1
				zoomAmnt+=0.1
			

		if Keys[pygame.K_e] and zoomAmnt < 5: # if zoom keys such as Q or E are being pressed
			for sprite in WorldGen.cameraSprites.sprites():
				zoomAmnt-=0.1
				sprite.rect.x = sprite.rect.x / 1.1
				sprite.rect.y = sprite.rect.y / 1.1
				zoomAmnt+=0.1

		display.fill((137, 207, 240)) # this refills the window with the sky colour

		WorldGen.cameraSprites.update()
		WorldGen.cameraSprites.draw(display) # this draws the new coordinates of the map over

		screen.blit(pygame.transform.scale(display, screen.get_size()), (0, 0))

		pygame.display.update()
		clock.tick(60)

#ogSize = sprite.image.get_size()
#print(ogSize)
#newSprite = sprite.image.convert() 
#newImage = pygame.transform.scale(newSprite, (int(ogSize[0]/zoomAmnt), int(ogSize[1]/zoomAmnt) ))