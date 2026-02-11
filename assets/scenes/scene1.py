from ursina import Entity, color



class MyMap(Entity):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.model = 'plane'
        # texture=
        self.scale = (20, 1, 20)
        self.color = color.blue
        # self.texture = 'assets/textures/map.png'