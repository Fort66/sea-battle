from ursina import *

app = Ursina()

camera.position = (0, 70, 0)
camera.rotation = (90, 0, 0)


ground = Entity(
    model='plane', 
    scale=(20, 1, 20), 
    collider='box',
    color=color.blue
)

cube = Entity(
    model='cube',
    color=color.orange,
    scale=1,
    position=(0, 0.5, 0),
    collider='box'
)

is_dragging = False

def input(key):
    global is_dragging

    if key == 'left mouse down':
        if mouse.hovered_entity == cube:
            is_dragging = True

    if key == 'left mouse up':
        is_dragging = False

def update():
    global is_dragging

    if is_dragging and held_keys['left mouse']:
        if mouse.world_point:
            cube.position = (mouse.world_point.x, cube.y, mouse.world_point.z)

app.run()