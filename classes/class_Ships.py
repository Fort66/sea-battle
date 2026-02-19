from ursina import Entity, Vec3, color, mouse, camera, scene

# sensitivity = 2
from icecream import ic
class Ships(Entity):
    def __init__(
        self,
        water=None,
        model=None,
        texture=None,
        scale=1,
        position=Vec3(0, 0, 0),
        rotation=Vec3(0, 0, 0),
        deck_amount=0
    ):
        super().__init__(
            model=model,
            texture=texture,
            scale=scale,
            position=position,
            rotation=rotation,
            collider="box"
        )

        self.water = water
        self.model = model
        self.texture = texture
        self.scale = scale
        self.position = position
        self.rotation = rotation
        self.deck_amount = deck_amount
        self.following_mouse = False
        self.is_selected = False

        self.is_grabbed = True

    def input(self, key):
        if self.is_grabbed:
            if key == 'left mouse down':
                if mouse.hovered_entity == self:
                    self.following_mouse = True
                    self.is_selected = True

            if key == 'left mouse up':
                self.following_mouse = False
                self.is_selected = False
                # ic(self.world_position)
                # ic(self)

            if key == 'right mouse down':
                if self.is_selected:
                    self.rotation += Vec3(0, 90, 0)

    def update(self):
        if self.following_mouse:
            self.position = Vec3(mouse.world_point[0], 0, mouse.world_point[2])

