import pygame
import os
pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((1080, 900))
x = 100
y = 100
kąt = 0

auto1 = pygame.image.load("auto1.png")
pygame.transform.scale(auto1, (150, 150))

auto2 = pygame.image.load("auto2.png")
pygame.transform.scale(auto2, (150, 150))

auto3 = pygame.image.load("auto3.png")
pygame.transform.scale(auto3, (150, 150))

auto = auto3
auto = pygame.transform.scale(auto, (150, 150))
v = 5
z = 0
angle = 0
left = -1
right = 1

run = True
while run:

  pygame.time.delay(10)
  screen.blit(pygame.transform.rotate(auto, angle), (x, y))
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
  keys = pygame.key.get_pressed()


  if keys[pygame.K_UP]:
    y = y + v - z
    x = x + z

  if keys[pygame.K_DOWN]:
      y = y - v + z
      x = x +v - z

  if keys[pygame.K_LEFT]:
    z = z + 0.1
    angle += 1
    angle %= 360

  if keys[pygame.K_RIGHT]:
    z = z - 0.1
    angle += -1
    angle %= 360

  if keys[pygame.K_ESCAPE]:
    pygame.quit()

  pygame.display.flip()
  clock.tick(120)
  screen.fill((0, 0, 0))
pygame.quit()