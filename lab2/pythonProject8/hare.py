import pygame

pygame.init()
FPS = 30
screen = pygame.display.set_mode((400,400))


# Цвета
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
DARK_GRAY = (150, 150, 150)
PINK = (255, 192, 203)
BLACK = (0, 0, 0)

# Основной цикл
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Заливка фона
    screen.fill(WHITE)

    # Задние лапы (рисуем под телом)
    pygame.draw.ellipse(screen, DARK_GRAY, (130, 300, 40, 100))  # Левая
    pygame.draw.ellipse(screen, DARK_GRAY, (230, 300, 40, 100))  # Правая

    # Тело зайца (эллипс)
    pygame.draw.ellipse(screen, GRAY, (135, 180, 130, 200))

    # Голова (круг)
    pygame.draw.circle(screen, GRAY, (200, 150), 50)

    # Передние лапы (рисуем поверх тела)
    pygame.draw.ellipse(screen,  DARK_GRAY, (170, 350, 20, 50))  # Левая
    pygame.draw.ellipse(screen,  DARK_GRAY, (210, 350, 20, 50))  # Правая

    # Уши
    pygame.draw.ellipse(screen, GRAY, (145, 30, 37, 100))  # Левое
    pygame.draw.ellipse(screen, PINK, (155, 45, 22, 75))
    pygame.draw.ellipse(screen, GRAY, (217, 30, 37, 100))  # Правое
    pygame.draw.ellipse(screen, PINK, (227, 45, 22, 75))

    # Глаза
    pygame.draw.circle(screen, BLACK, (175, 135), 8)
    pygame.draw.circle(screen, BLACK, (225, 135), 8)

    # Нос
    pygame.draw.polygon(screen, PINK, [(200, 160), (195, 170), (205, 170)])

    # Усы
    pygame.draw.line(screen, BLACK, (195, 170), (150, 155), 1)
    pygame.draw.line(screen, BLACK, (195, 175), (150, 175), 1)
    pygame.draw.line(screen, BLACK, (195, 177), (150, 195), 1)
    pygame.draw.line(screen, BLACK, (205, 170), (250, 155), 1)
    pygame.draw.line(screen, BLACK, (205, 175), (250, 175), 1)
    pygame.draw.line(screen, BLACK, (205, 177), (250, 195), 1)
    # Обновление экрана
    pygame.display.update()
    clock = pygame.time.Clock()
    finished = False

    while not finished:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True

    pygame.quit()

pygame.quit()