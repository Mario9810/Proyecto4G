import pygame
from pygame.locals import *

from gl import Renderer, Model
import shaders

deltaTime = 0.0

# Inicializacion de pygame
pygame.init()
clock = pygame.time.Clock()
screenSize = (960, 540)
screen = pygame.display.set_mode(screenSize, DOUBLEBUF | OPENGL)

#musica 
pygame.mixer.music.load("ClaireDeLune.mp3")
pygame.mixer.music.play(-1)
#modelos 
modelos = [
        {
            'nameFile': 'model.obj',
            'textureFile': 'model.bmp',
            'init': 3,
        },
        {
            'nameFile': 'tv.obj',
            'textureFile': 'tv.bmp',
            'init': 10,
        },
        {
            'nameFile': 'Panda.obj',
            'textureFile': 'pandas.bmp',
            'init': 12,
        },
        {
            'nameFile': 'bear.obj',
            'textureFile': 'bearskin.bmp',
            'init': 13,
        }]

# Inicializacion de nuestro Renderer en OpenGL
r = Renderer(screen)
r.pointLight.x = 5
r.pointLight.z = 88

r.camPosition.z = modelos[r.temp]['init']
r.setShaders(shaders.vertex_shader, shaders.fragment_shader)

for modelo in modelos:
    print(modelo['nameFile'])
    r.modelList.append(Model(modelo['nameFile'],modelo['textureFile']))
#r.modelList.append(Model('model.obj', 'model.bmp'))



isPlaying = True
while isPlaying:

    # Para revisar si una tecla esta presionada
    keys = pygame.key.get_pressed()
    click = pygame.mouse.get_pressed()
    mos = pygame.mouse.get_pos()
    # Move cam
    if keys[K_d]:
        r.modelList[r.temp].rotation.z -= 1
    if keys[K_a]:
        r.modelList[r.temp].rotation.z += 1
    if keys[K_w]:
        r.modelList[r.temp].rotation.x += 1
    if keys[K_s]:
        r.modelList[r.temp].rotation.x -= 1
    if click[0] and mos[0]>480:
        r.modelList[r.temp].rotation.y += 1 
                
    if click[0] and (480>mos[0]>0):
        r.modelList[r.temp].rotation.y -= 1

    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            isPlaying = False
        elif ev.type == pygame.KEYDOWN:
            # para revisar en el momento que se presiona una tecla
            if ev.key == pygame.K_1:
                r.filledMode()
            elif ev.key == pygame.K_2:
                r.wireframeMode()
            elif ev.key == pygame.K_ESCAPE:
                isPlaying = False
            elif ev.key == pygame.K_3 or ev.key == pygame.K_KP1:
                r.temp = 0
                r.camPosition.z = modelos[r.temp]['init']
            elif ev.key == pygame.K_4 or ev.key == pygame.K_KP2:
                r.temp = 1
                r.camPosition.z = modelos[r.temp]['init']
            elif ev.key == pygame.K_5 or ev.key == pygame.K_KP3:
                r.temp = 2
                r.camPosition.z = modelos[r.temp]['init']
            elif ev.key == pygame.K_6 or ev.key == pygame.K_KP4:
                r.temp = 3
                r.camPosition.z = modelos[r.temp]['init']
            
    

    # Main Renderer Loop
    r.render()

    pygame.display.flip()
    clock.tick(60)
    deltaTime = clock.get_time() / 1000


pygame.quit()
