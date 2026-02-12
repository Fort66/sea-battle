from ursina import Text, color, Button


class SceneText(Text):
    def __init__(self):
        super().__init__(
            text='a',
            color=color.white,
            position=(-.75, 0, 0),
            scale=2,
            rotation=(30, 45, 0)
        )


class SceneButton(Button):
    def __init__(self):
        super().__init__(
            text='a',
            color=color.gray,
            position=(-.75, 0, 0),
            scale=(.5, 0, .5),
        )