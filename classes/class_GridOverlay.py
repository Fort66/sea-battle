from ursina import Entity, color, Vec3, Grid

class GridOverlay(Entity):
    def __init__(self, **kwargs):
        super().__init__(
            model=Grid(
                width=10,
                height=10,
                thickness=3
            ),
            scale=10,
            color=color.black,
            position=Vec3(0, .002, 5),
            rotation=Vec3(90, 0, 0)
        )