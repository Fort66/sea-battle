from ursina import Entity, Text, color, Vec3

from string import ascii_letters


class CoordinatesText:
    def __init__(self, grid):
        self.letters_list = [ascii_letters[i] for i in range(10)]
        self.digits_list = [str(i) for i in range(1, 11)]
        self.grid = grid

        self.set_coordinates()

    def draw_coourinates(self, iteration_object, idx, cell):
        Entity(
            model=Text(
                text=iteration_object[idx],
                color=color.white,
            ),
            scale=20,
            rotation=Vec3(90, 0, 0),
        ).position = self.grid.map_position_cells[cell][0]

    def set_coordinates(self):
        for i in range(1, 11):
            self.draw_coourinates(self.letters_list, (i - 1), (i, 11))
            self.draw_coourinates(self.letters_list, (i - 1), (i, 0))
            self.draw_coourinates(self.digits_list, (i - 1), (11, i))
            self.draw_coourinates(self.digits_list, (i - 1), (0, i))


