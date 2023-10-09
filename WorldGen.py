import math, os, random, CameraHandler, pygame, LivePlayer

ReferenceMap = [] # 2d array which contains a reference to every tile. This can be used to determine if there's something on the tile or not
cameraSprites = pygame.sprite.Group()

# creates a binary file, where 1 means there is a tile, 0 means no tile
def createWorldFile(x,y, worldName): # takes x, y and the name of the world so it can be loaded later on
    os.mkdir(f"C:/Users/Tristan/Desktop/A Level and Programming/A-Level/A-Level compsci/ProgrammingProject/PlayerWorlds/{worldName}")
    NewFile = open(f"C:/Users/Tristan/Desktop/A Level and Programming/A-Level/A-Level compsci/ProgrammingProject/PlayerWorlds/{worldName}/{worldName}#WORLD.txt", mode="w")
    for xSize in range(x): 
        NewFile.write("1"), 
        for ySize in range(y):
            NewFile.write("1")
        NewFile.write("\n")
    NewFile.write("\n")
    NewFile.close()
    
def createRivers(filePath):
    FileToOverWrite = open(filePath)
    map_data = [[int(i) for i in row] for row in FileToOverWrite.read().split('\n')] # gets the map data as an array. we're going to change this array, then rewrite the changes

    Alternate =  random.randint(0, math.ceil(len(map_data)/2))# number to increase/decrease position by, as well as the starting point of the river
    ##### CODE TO OVERWRITE THE LIST ##### 
    for line in map_data: # for every line
        try:
            line[Alternate] = "0"
            for i in range(2):
                line[Alternate+i+1]="0"
            Alternate+=random.randint(-2,2)
        except IndexError:
            pass
    ### C0DE TO WRITE THE LIST TO THE FILE ####
    FileToOverWrite = open(filePath, mode="w")
    for line in map_data:
        for item in line:
            FileToOverWrite.write(str(item))
        FileToOverWrite.write("\n")
    FileToOverWrite.close()

def createFoliage(filePath, worldName):
    fileToReference = open(filePath)
    FoliageFile = open(f"C:/Users/Tristan/Desktop/A Level and Programming/A-Level/A-Level compsci/ProgrammingProject/PlayerWorlds/{worldName}/{worldName}#FOLIAGE.txt", mode="w")

    map_data = [[int(i) for i in row] for row in fileToReference.read().split('\n')]
    for line in map_data:
        for i in range(len(line)):
            if line[i]==1: # if its a ground tile
                FoliageFile.write(str(random.randint(0,1))) # choose randomly if foliage is added (1 is a tree, 0 id no tree)
            elif line[i]==0: # if its a water tile
                FoliageFile.write(str("0")) # If its a water tile, there's no foliage on it in the first place
        FoliageFile.write("\n")

def drawMap(display, name, spriteAtlas): # display is the pygame display (the screen), name is the name of the world to load, SpriteAtlas is the sprites for grass
    display.fill((137, 207, 240)) # RGB for baby blue, a nice background color

    mapFile = open(f'C:/Users/Tristan/Desktop/A Level and Programming/A-Level/A-Level compsci/ProgrammingProject/PlayerWorlds/{name}/{name}#WORLD.txt')
    map_data = [[int(i) for i in row] for row in mapFile.read().split('\n')] # get the binary file into a list
    mapFile.close()

    foliageFile = open(f'C:/Users/Tristan/Desktop/A Level and Programming/A-Level/A-Level compsci/ProgrammingProject/PlayerWorlds/{name}/{name}#FOLIAGE.txt')
    foliage_data = [[int(i) for i in row] for row in foliageFile.read().split('\n')] # doing the same for foliage than i am for the world
    foliageFile.close()

    #display.blit(tileToDisplay, (150 + x * 10 - y * 10, 100 + x * 5 + y * 5)) # this uses Pygame.Surface, which cannot be added to a sprite group
    #cameraSprites.add(tileToDisplay) # instead, i've tried to convert these 'surfaces' to sprites

    # THIS FOR LOOP IS THE ONLY CODE I GOT OFF THE INTERNET. EVERYTHING ELSE IS MY OWN WORK (I only used the math offset and enumrate parts out of the large script by DaFluffyPotato on YouTube)
    for y, row in enumerate(map_data): # enumarate through the list of binary
        for x, tile in enumerate(row):
            ReferenceMap.append(f"{y},{x}") # add to the mapReference to make coordinates easier
            if tile:
                tileToDisplay = pygame.sprite.Sprite()
                tileToDisplay.image = random.choice(spriteAtlas[0])

                tileToDisplay.rect = tileToDisplay.image.get_rect()

                tileToDisplay.rect.x = (150 + x * 10 - y * 10)
                tileToDisplay.rect.y = (100 + x * 5 + y * 5)

                cameraSprites.add(tileToDisplay)
            elif not tile:
                tileToDisplay = pygame.sprite.Sprite()
                tileToDisplay.image = random.choice(spriteAtlas[2])

                tileToDisplay.rect = tileToDisplay.image.get_rect()

                tileToDisplay.rect.x = (150 + x * 10 - y * 10)
                tileToDisplay.rect.y = (100 + x * 5 + y * 5)

                cameraSprites.add(tileToDisplay)
    
    for y, row in enumerate(foliage_data): # enumarate through the list of binary
            for x, foliage in enumerate(row):
                if foliage:
                    foliageToDisplay = pygame.sprite.Sprite()
                    foliageToDisplay.image = random.choice(spriteAtlas[1])

                    foliageToDisplay.rect = tileToDisplay.image.get_rect()

                    foliageToDisplay.rect.x = (150 + x * 10 - y * 10)
                    foliageToDisplay.rect.y = (100 + x * 5 + y * 5 - 14)

                    cameraSprites.add(foliageToDisplay)

    cameraSprites.draw(LivePlayer.display)
    print("Map generated!")

if __name__ == "__main__":
    print("lol")