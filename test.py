from ursina import *  
  
app = Ursina()  
  
# Создаем объект с коллайдером  
draggable = Entity(model='cube', color=color.red, collider='box')  
  
def on_click():  
    draggable.following_mouse = True  # Начать следование за мышью  
  
draggable.on_click = on_click  
draggable.following_mouse = False  # Изначально не следует  
  
def update():  
    if draggable.following_mouse:  
        # Для UI объектов (parent=camera.ui)  
        draggable.position = mouse.position  
          
        # Для 3D объектов нужно преобразовать в мировые координаты  
        # draggable.world_position = mouse.world_point  

EditorCamera()
app.run()