from ursina import *
from assets.scenes.scene1 import MyMap

from ursina.editor.level_editor import LevelEditor

if __name__ == "__main__":
    window.vsync = False

    # my_map = MyMap()
    app = Ursina()

    # Создаем плоскость с сеткой
    grid_size = 10
    ground = Entity(
        model='plane', 
        scale=grid_size, 
        texture='white_cube',
        collider='box',
        color=color.gray
    )

    # Визуальная сетка поверх
    grid_overlay = Entity(
        model=Grid(grid_size, grid_size), 
        rotation_x=90, 
        scale=grid_size, 
        color=color.white33
    )

    def input(key):
        if key == 'left mouse down':
            if mouse.hovered_entity == ground:
                # Переводим их в диапазон от 0 до grid_size
                hit_pos = mouse.point - ground.world_position
                x = int((hit_pos.x + ground.scale_x / 2) / (ground.scale_x / grid_size))
                z = int((hit_pos.z + ground.scale_z / 2) / (ground.scale_z / grid_size))
                
                print(f"Клик по ячейке: X={x}, Z={z}")
                
                # Пример: ставим блок в центр ячейки
                Entity(model='cube', color=color.orange, scale=0.5, 
                    position=(x - grid_size/2 + 0.5, 0.25, z - grid_size/2 + 0.5))

    # center = Entity(model='quad', scale=.025, color=color.red, always_on_top=True)
    # p = Entity()
    # for i in range(13):
    #     b = Button(parent=p, model='quad', scale=Vec2(.2,.1), text=str(i), color=color.tint(color.random_color(),-.6))
    #     b.text_entity.scale=1
    # t = time.time()
    # grid_layout(p.children, origin=(0,.5), spacing=(.1,.1))
    # center = Entity(parent=camera.ui, model=Circle(), scale=.005, color=color.lime)
    # EditorCamera()
    # print(time.time() - t)

    # for e in [(-.5,.5), (0,.5), (.5,.5), (-.5,0), (0,0), (.5,0), (-.5,-.5), (0,-.5), (.5,-.5)]:
    #     Button(text='*', model='quad', text_origin=e, scale=.095, origin=(-.5,.5), position = window.top_left + Vec2(*e)*.2 + Vec2(.1,-.1), tooltip=Tooltip(str(e)),
    #         on_click=Func(grid_layout, p.children, max_x=4, origin=e, spacing=(.05,.05))
    #     )



    def update():
        pass

    EditorCamera()

    app.run()
