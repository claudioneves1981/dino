from ursina import *
import random


app = Ursina()
window.title = 'Dino'
window.color = color.white
camera.orthographic = True
camera.fov = 5

camera.x, camera.y = 2.6, 1.7
CINZA = color.rgb32(83, 83, 83)
Entity(model='quad', color=CINZA, scale=(40,0.05))

dino = Entity()
PARTES = [(0, 0.6,0.6,0.6),
          (0.35, 1.05, 0.5, 0.35),
          (-0.15, 0.15, 0.12,0.3),
          (0.15, 0.15, 0.12,0.3),
          (-0.4,0.75, 0.3, 0.15)]
for x, y, w, h in PARTES:
    Entity(parent=dino, model='quad', color=CINZA, x=x, y=y, scale=(w,h))

Entity(parent=dino, model='quad', color=color.white, x=0.45, y=1.1, z=-0.1, scale=(0.08))

def novo_cacto(x):          
    largura = random.uniform(0.25, 0.5)
    altura =  random.uniform(0.6, 1.1)
    return Entity(model='quad', color=CINZA, origin_y=-0.5, x=x, scale=(largura, altura))

cactos = [novo_cacto(9+i*7) for i in range(3)]
pontos = 0
placar = Text('00000',scale=2, position=(0.42,0.45),color=CINZA)
aviso = Text('', scale=3, origin=(0,0), color=CINZA)

def bateu(c):
    return abs(c.x - dino.x) <  c.scale_x/2 + 0.3 and dino.y < c.scale_y

vel = 0
velocidade = 6

def update():
    global vel, velocidade, pontos
    vel -= 30 * time.dt
    dino.y = max(dino.y + vel * time.dt, 0)
    pontos += 10 * time.dt
    velocidade = 6 + pontos / 100
    placar.text = f'{int(pontos):05}'
    for c in cactos:
        c.x -= velocidade * time.dt
        if c.x < -2:
            fim = max(o.x for o in cactos)
            c.x = fim + random.uniform(5, 9)
        if bateu(c):
            aviso.text = 'GAME OVER'
            application.pause()

def input(key):
    global vel
    if key == 'space' and dino.y == 0:
        vel = 11

app.run()
