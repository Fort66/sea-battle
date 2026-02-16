from ursina import Button, camera, Vec3, color


class NavButton(Button):
    def __init__(
        self,
        text='Click',
        position=(0, .4, 0),
        scale=.1,
        color=color.blue,
        **kwargs
    ):

        super().__init__(
            text=text,
            scale=scale,
            position=position,
            color=color,
            **kwargs
        )

        self.enemy_position = False
        self.on_click = self.change_value

    def change_value(self):
        self.enemy_position = not self.enemy_position