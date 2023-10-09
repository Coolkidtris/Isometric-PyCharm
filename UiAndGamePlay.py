import pygame, WorldGen, CameraHandler, LivePlayer, time

year = 1900
month = 1
day = 1

timePaused = False
timeSpeed = 3 # speed at which the days, months and years increase

def increaseTime():
    global month
    global day
    global year
    while timePaused == False: # while time is running and not paused
        time.sleep(.25/timeSpeed)
        day+=1
        if day == 31 or timeSpeed == 3:
            day = 1
            month+=1
        if month == 13:
            month = 1
            year +=1
        
        print(f"{day}/{month}/{year}")

def clickCard(mousePos):
    for item in WorldGen.cameraSprites.sprites():
        itemRect = item.rect
        print("")
        if pygame.mouse.get_pressed()[0] and itemRect.collidepoint(mousePos):
            print("Card clicked")