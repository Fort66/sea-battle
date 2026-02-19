from ursina import *

from icecream import ic


from classes.create_objects import my_water_area, my_grid_overlay,my_lower_grid, my_coordinates, enemy_water_area, enemy_grid_overlay, enemy_lower_grid, enemy_coordinates, nav_button, four_deck_menu

from classes.class_ShipsCreator import ShipsCreator

my_ships_creator = ShipsCreator()

# enemy_ships_creator = ShipsCreator()

if __name__ == "__main__":
    window.vsync = False
    app = Ursina()



    ambient_lights = AmbientLight(color=color.white)
    # EditorCamera()
    # camera.parent = my_water_area
    # camera.rotation = Vec3(35, 0, 0)
    # camera.position = Vec3(0, 15, 0)
    # camera.fov = 60

    camera.position = Vec3(0, 15, -22)
    camera.rotation = Vec3(35, 0, 0)
    # camera.fov = 60

    def update():
        my_ships_creator.update()

        if nav_button.enemy_position:
            if camera.position.x > enemy_water_area.position.x:
                camera.position -= Vec3(20, 0, 0) * time.dt
        else:
            if camera.position.x < my_water_area.position.x:
                camera.position += Vec3(20, 0, 0) * time.dt

    app.run()
