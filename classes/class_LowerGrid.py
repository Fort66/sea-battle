from ursina import Entity, color, Vec3, Grid

class LowerGrid(Entity):
    def __init__(self, **kwargs):
        super().__init__(
            model=Grid(
                width=11,
                height=11,
                thickness=3
            ),
            scale=11,
            color=color.rgba(0, 0, 0, 0.1),
            position=Vec3(-.52, -.02, 5.58),
            rotation=Vec3(90, 0, 0)
        )