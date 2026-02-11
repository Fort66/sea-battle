from ursina import *
from assets.scenes.scene1 import MyMap

from ursina.editor.level_editor import LevelEditor

if __name__ == "__main__":
    window.vsync = False

    my_map = MyMap()
    app = Ursina()


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
