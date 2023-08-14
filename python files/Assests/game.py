import pgzrun

HEIGHT = 600
WIDTH = 1100
w, h = WIDTH, HEIGHT
music.play('remix')

i = Actor('ironman', (w//2, h//2))
e = Actor('alien', (w//2, 200))
c = Actor('coin', (w//2, h-100))

def draw():
    screen.fill('black')
    i.draw()
    e.draw()
    c.draw()

def player_update():
    if keyboard.left:
        i.x -= 5
    elif keyboard.right:
        i.x += 5
    elif keyboard.up:
        i.y -= 5
    elif keyboard.down:
        i.y += 5

def enemy_update():
    e.x += 5
    if e.x > w:
        e.x = 0

def update():
    enemy_update()
    player_update()

pgzrun.go()