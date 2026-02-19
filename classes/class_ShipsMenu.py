from ursina import Entity, Vec3, color, mouse, camera, scene

from .class_ShipsCreator import ShipsCreator

ships_creater = ShipsCreator()

class ShipsMenu(Entity):
    def __init__(
        self,
        water=None,
        model=None,
        texture=None,
        scale=1,
        position=Vec3(0, 0, 0),
        rotation=Vec3(0, 0, 0),
        ship_counter=0,
        deck_amount=0,
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
        self.ship_counter = ship_counter
        self.deck_amount = deck_amount

        self.is_grabbed = False

    def input(self, key):
        if key == 'left mouse down':
            if mouse.hovered_entity == self:
                self.ship_counter -= 1
                ships_creater.count_deck = self.deck_amount
                ships_creater.create_ship_command = True
                ships_creater.model = self.model.name
                ships_creater.texture = self.texture
                ships_creater.water = self.water

        if self.ship_counter <= 0:
            self.visible = False



