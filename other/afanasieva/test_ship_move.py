from ursina import *

app = Ursina()

camera.position = (0, 60, 0)
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

snap_points = [
    Vec3(5, 0.5, 5),
    Vec3(-5, 0.5, 5),
    Vec3(5, 0.5, -5),
    Vec3(-5, 0.5, -5)
]

for p in snap_points:
    Entity(model='sphere', color=color.white, scale=0.5, position=p)

is_dragging = False

def input(key):
    global is_dragging

    if key == 'left mouse down':
        if mouse.hovered_entity == cube:
            is_dragging = True

    if key == 'left mouse up':
        if is_dragging:
            is_dragging = False
            nearest_point = snap_points[0]
            min_dist = distance(cube.position, snap_points[0])

            for p in snap_points:
                dist = distance(cube.position, p)
                if dist < min_dist:
                    min_dist = dist
                    nearest_point = p
            
            cube.position = nearest_point

def update():
    global is_dragging

    if is_dragging and held_keys['left mouse']:
        if mouse.world_point:
            cube.position = Vec3(mouse.world_point.x, cube.y, mouse.world_point.z)

app.run()
