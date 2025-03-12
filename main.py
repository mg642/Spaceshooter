# Skriv din kod här för att skapa spelet! Följ dessa steg:
'''
Steg 1 - Skapa en skärm och rita ett skepp
Steg 2 - Lägga till en scrollande stjärnbakgrund
Steg 3 - Sätt jetmotorer på rymdskeppet
Steg 4 - Gör så rymdskeppet kan skjuta
Steg 5 - Slumpa fram Asteroider 
Steg 6 - Detektera kollisioner mellan rymdskeppet och asteroiden
Steg 7 - Skapa explosionseffekten (samt lär dig partikeleffekter)
Steg 8 - Gör så att rymdskeppet kan explodera i kollision med asteroiden
Steg 9 - Gör så att rymdskeppet kan skjuta ner asteroider
Steg 10 - Lägg till musik och ljudeffekter
'''

import pygame
pygame.init()

SKÄRMENS_BREDD = 660
SKÄRMENS_HÖJD = 660

skärm = pygame.display.set_mode((SKÄRMENS_BREDD, SKÄRMENS_HÖJD))

pygame.display.set_caption("Space Shooter")

original_bild = pygame.image.load ("assets/sprites/spaceShip.png")
sprite_spelare = pygame.transform.scale(original_bild, (original_bild.get_width() // 2, original_bild.get_height() // 2))

background_mörkblå = pygame.image.load("assets/backgrounds/bg.png") 
background_stjärnor = pygame.image.load("assets/backgrounds/Stars-A.png")

bakgrund_y = 0 

spelare_x = SKÄRMENS_BREDD // 2 - 120  
spelare_y = SKÄRMENS_HÖJD - 200
spelarens_hastighet = 1 

spelet_körs = True
while (spelet_körs == True): 
    skärm.fill((0, 0, 30))

    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            spelet_körs = False

    
    # Ritar alla bakgrunder
    skärm.blit(background_mörkblå, (0,0))
    skärm.blit(background_stjärnor, (0, bakgrund_y))
    skärm.blit(background_stjärnor, (0, bakgrund_y - SKÄRMENS_HÖJD))
    
    bakgrund_y = bakgrund_y + 20 
  

    if bakgrund_y >= SKÄRMENS_HÖJD:
        bakgrund_y = 0 


    #Ritar alla spelfigurer
    skärm.blit(sprite_spelare, (spelare_x, spelare_y))

    sprite_jetstråle = pygame.image.load("assets/sprites/fire.png")
    jetstråle_x = spelare_x + 13
    jetstråle_y = spelare_y + 46

    keys = pygame.key.get_pressed()
if keys[pygame.K_LEFT] and spelare_x > 0:
    spelare_x = spelare_x - spelarens_hastighet 
    jetstråle_x = jetstråle_x - spelarens_hastighet 
if keys[pygame.K_RIGHT] and spelare_x < SKÄRMENS_BREDD - sprite_spelare.get_width():
    spelare_x = spelare_x + spelarens_hastighet 
    jetstråle_x = jetstråle_x + spelarens_hastighet 
if keys[pygame.K_UP] and spelare_y > 0: 
    spelare_y = spelare_y - spelarens_hastighet 
    jetstråle_y = jetstråle_y - spelarens_hastighet
if keys[pygame.K_DOWN] and spelare_y < SKÄRMENS_HÖJD - sprite_spelare.get_width() - 20:
    spelare_y = spelare_y + spelarens_hastighet 
    jetstråle_y = jetstråle_y + spelarens_hastighet 

screen.blit(sprite_jetstråle, (jetstråle_x, jetstråle_y))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and spelare_x > 0:
        spelare_x = spelare_x - spelarens_hastighet 
    if keys[pygame.K_RIGHT] and spelare_x < SKÄRMENS_BREDD - sprite_spelare.get_width():
        spelare_x = spelare_x + spelarens_hastighet
    if keys[pygame.K_UP] and spelare_y > 0:
        spelare_y = spelare_y - spelarens_hastighet
    if keys[pygame.K_DOWN] and spelare_y < SKÄRMENS_HÖJD - sprite_spelare.get_width() + 26:
        spelare_y = spelare_y + spelarens_hastighet






    pygame.display.update()


pygame.quit()