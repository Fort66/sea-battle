from ursina import Entity, Vec3, color, mouse, camera, scene

from .class_Ships import Ships

# from .create_objects import my_water_area

from icecream import ic

class ShipsCreator:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls, *args, **kwargs)
        return cls.__instance

    def __init__(self, water=None):
        self.water = water
        self.create_ship_command = False
        self.count_deck = 0
        self.model=None
        self.texture=None
        self.ships = []

    def update(self):
        if self.create_ship_command:
            self.ships.append(
                Ships(
                    model=self.model,
                    texture=self.texture,
                    scale=.015,
                    # position=Vec3(0, 0, 0),
                    position=self.water.map_position_cells[(7, 5)][0],
                    rotation=(90, 90, 0),
                    deck_amount=4
                )
            )
            self.create_ship_command = False
            self.count_deck = 0
            self.model = None
            self.texture = None
