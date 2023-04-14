import pygame

pygame.init()
pygame.mixer.init()
STOPPED_PLAYING = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(STOPPED_PLAYING)
musicnumber = 0

musics = ['music1.mp3', 'music2.mp3']  # список имен файлов

HEIGHT, WIDTH = 500, 500
screen = pygame.display.set_mode((HEIGHT, WIDTH))

pygame.mixer.music.load(musics[0])  # Эта функция загружает первую музыку из списка в плеер
pygame.mixer.music.play()

x = 0
y = 0.5
running = True
while running:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE and x == 0:
                pygame.mixer.music.pause()
                x = 1
            elif event.key == pygame.K_SPACE and x == 1:
                pygame.mixer.music.unpause()
                x = 0
            elif event.key == pygame.K_LEFT:
                musicnumber = (musicnumber + 10) % 11
                print(musicnumber)
                pygame.mixer.music.load(musics[musicnumber])
                pygame.mixer.music.play()
            elif event.key == pygame.K_RIGHT:
                musicnumber = (musicnumber + 1) % 11
                print(musicnumber)
                pygame.mixer.music.load(musics[musicnumber])
                pygame.mixer.music.play()
            elif event.key == pygame.K_UP and y <= 1:
                y += 0.1
                pygame.mixer.music.set_volume(y)
            elif event.key == pygame.K_DOWN and y >= 0:
                y -= 0.1
                pygame.mixer.music.set_volume(y)
        elif event.type == STOPPED_PLAYING:
            musicnumber = (musicnumber + 1) % 10
            pygame.mixer.music.load(musics[musicnumber])
            pygame.mixer.music.play()

    # Отрисовка шкалы громкости
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(50, 400, y * 400, 20))  # Зеленый прямоугольник - шкала громкости
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(50, 400, 400, 20),
                     2)  # Черный контур прямоугольника - границы шкалы
    pygame.display.set_caption(musics[musicnumber][6:(len(musics[musicnumber]) - 4)])
    pygame.display.flip()

pygame.quit()
