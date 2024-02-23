import pygame, random, time, asyncio

pygame.init()

width, height = 1120, 630
win = pygame.display.set_mode((width, height))
pygame.display.set_caption('Reanimated')

clock = pygame.time.Clock()

bg = pygame.transform.scale(pygame.image.load("resources\\bg.png"), (width, height))
player = pygame.transform.scale(pygame.image.load("resources\\player.png"), (20, 20))
plyrect = player.get_rect(topleft = (1100, 200))
spike = pygame.transform.scale(pygame.image.load("resources\\spike.png"), (20, 20))
spikerect = spike.get_rect(topleft = (100, 100))
spike1 = pygame.transform.scale(pygame.image.load("resources\\spike.png"), (20, 20))
spike1rect = spike.get_rect(topleft = (100, 100))
spike2 = pygame.transform.scale(pygame.image.load("resources\\spike.png"), (20, 20))
spike2rect = spike.get_rect(topleft = (200, 200))
spike3 = pygame.transform.scale(pygame.image.load("resources\\spike.png"), (20, 20))
spike3rect = spike.get_rect(topleft = (300, 300))

pygame.mixer.music.load("resources\\bgm.mp3")
pygame.mixer.music.play(-1)

font = pygame.font.Font('freesansbold.ttf', 128)
text = font.render('YOU DIED', True, 'red')
deathrect = text.get_rect(center = (1060, 3110))

def draw():
    win.blit(bg, (0, 0))
    win.blit(player, plyrect)
    win.blit(spike, spikerect)
    win.blit(spike1, spike1rect)
    win.blit(spike2, spike2rect)
    win.blit(spike3, spike3rect)
    win.blit(scoretext, scorerect)
    pygame.display.update()

async def main():
    global scoretext, scorerect
    x = 0
    print('game launched')
    playery = 0
    playerx = 0
    spikey = -10
    spikex = 10
    spike1y = 10
    spike1x = 10
    spike2y = -10
    spike2x = -10
    spike3y = 10
    spike3x = -10
    score = 0
    displayedscore = 0
    run = True
    runnow = True
    while runnow and run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runnow = False
                break
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                runnow = False
                break
        plyrect.y += playery
        plyrect.x += playerx
        spikerect.y += spikey
        spikerect.x += spikex
        spike1rect.y += spike1y
        spike1rect.x += spike1x
        spike2rect.y += spike2y
        spike2rect.x += spike2x
        spike3rect.y += spike3y
        spike3rect.x += spike3x
        
        scoretext = font.render(str(displayedscore), True, 'white')
        scorerect = scoretext.get_rect(topright = (1120, 0))

        if run:
            if plyrect.top < 0:
                plyrect.bottom = 629
            elif plyrect.bottom > 630:
                plyrect.top = 1
            elif plyrect.left < 0:
                plyrect.right = 1119
            elif plyrect.right > 1120:
                plyrect.left = 1

            if spikerect.top < 0:
                spikey = 10
            elif spikerect.bottom > height:
                spikey = -10
            elif spikerect.left < 0:
                spikex = 10
            elif spikerect.right > width:
                spikex = -10
            

            if spike1rect.top < 0:
                spike1y = 10
            elif spike1rect.bottom > height:
                spike1y = -10
            elif spike1rect.left < 0:
                spike1x = 10
            elif spike1rect.right > width:
                spike1x = -10
            

            if spike2rect.top < 0:
                spike2y = 10
            elif spike2rect.bottom > height:
                spike2y = -10
            elif spike2rect.left < 0:
                spike2x = 10
            elif spike2rect.right > width:
                spike2x = -10
            
            if spike3rect.top < 0:
                spike3y = 10
            elif spike3rect.bottom > height:
                spike3y = -10
            elif spike3rect.left < 0:
                spike3x = 10
            elif spike3rect.right > width:
                spike3x = -10

        win.blit(player, plyrect)
        pygame.draw.rect(win, (0, 0, 0), plyrect)

        keys = pygame.key.get_pressed()
        if run:
            if keys[pygame.K_w]:
                playery = -5
            elif keys[pygame.K_s]:
                playery = 5
            elif keys[pygame.K_a]:
                playerx = -5
            elif keys[pygame.K_d]:
                playerx = 5

        draw()
        if pygame.Rect.colliderect(plyrect, spikerect) or pygame.Rect.colliderect(plyrect, spike1rect) or pygame.Rect.colliderect(plyrect, spike2rect) or pygame.Rect.colliderect(plyrect, spike3rect):
            win.blit(text, deathrect)
            run = False
            pygame.display.update()

        clock.tick(60)
        x += 1
        if x == 10:
            x = 0
            playerx = 0
            playery = 0
        score += 1
        if score == 60:
            score = 0
            displayedscore += 1
            print(displayedscore)
            win.blit(scoretext, scorerect)
            pygame.display.update()

    await asyncio.sleep(0)
    pygame.mixer.music.stop()
    pygame.quit()

asyncio.run(main())