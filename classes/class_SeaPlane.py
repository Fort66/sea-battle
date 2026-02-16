from ursina import Entity, color, Vec3
from ursina.shaders import lit_with_shadows_shader



class SeaPlane(Entity):
    def __init__(
        self,
        position=Vec3(0, 0, 0),
        rotation=Vec3(0, 0, 0),
        **kwargs,
        ):

        super().__init__(
        model = 'plane',
        texture='white_cube',
        scale = 10,
        color = color.blue,
        shader = lit_with_shadows_shader,
        position=position,
        rotation=rotation,
        )

        self.position = position
        self.rotation = rotation