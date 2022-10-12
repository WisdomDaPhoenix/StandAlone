import arcade
# arcade.open_window(1200,800,"My Game")
# arcade.set_background_color(arcade.color.BLACK)
# arcade.start_render()
# arcade.finish_render()
# arcade.run()


class MyGameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width,height,title,resizable=True)
        self.set_location(25,80)
        arcade.set_background_color(arcade.color.WHITE)
        self.arthur = arcade.Sprite("king_authur.png")
        self.blu_xpos = 150
        self.blu_ypos = 150
        self.yel_xpos = 300
        self.yel_ypos = 300
        self.gre_xpos = 450
        self.gre_ypos = 450
        self.setup()
    def setup(self):
        self.arthur.bottom = 550
        self.arthur.left = 1000
        self.arthur.scale = 0.5

    def on_draw(self):
        arcade.start_render()
        # arcade.draw_point(300,700,arcade.color.GOLD,5)
        # arcade.draw_line(0,0,100,100,arcade.color.BABY_BLUE,12)
        arcade.draw_circle_filled(self.blu_xpos,self.blu_ypos,50,arcade.color.BLUE,70)
        arcade.draw_circle_filled(self.yel_xpos, self.yel_ypos, 50, arcade.color.YELLOW, 70)
        arcade.draw_circle_outline(self.gre_xpos,self.gre_ypos,50,arcade.color.GREEN,6,70)
        arcade.draw_lrtb_rectangle_filled(500,600,600,500,arcade.color.GOLD)
        arcade.Sprite.draw(self.arthur)
    def on_update(self, delta_time):
        self.arthur.update()
    def on_key_press(self, key, modifiers):
        if key == arcade.key.RIGHT:
            self.arthur.change_x = 12
        elif key == arcade.key.LEFT:
            self.arthur.change_x = -12
        elif key == arcade.key.UP:
            self.arthur.change_y = 8
        elif key == arcade.key.DOWN:
            self.arthur.change_y = -8

    def on_key_release(self, key, modifiers):
        if key == arcade.key.RIGHT:
            self.arthur.change_x = 0
        elif key == arcade.key.LEFT:
            self.arthur.change_x = 0
        elif key == arcade.key.UP:
            self.arthur.change_y = 0
        elif key == arcade.key.DOWN:
            self.arthur.change_y = 0

    def on_mouse_press(self, x, y, button, modifiers ):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.blu_xpos = x
            self.blu_ypos = y
        elif button == arcade.MOUSE_BUTTON_RIGHT:
            self.yel_xpos = x
            self.yel_ypos = y

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        self.gre_xpos = x
        self.gre_ypos = y






MyGameWindow(1270,800,'Flying Birds')
arcade.run()

