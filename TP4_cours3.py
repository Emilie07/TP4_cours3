#Emilie Mancera

import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

COLORS = [arcade.color.AFRICAN_VIOLET, arcade.color.AMARANTH_PINK, arcade.color.ARYLIDE_YELLOW, arcade.color.BLEU_DE_FRANCE]

def balle(self, position_x, position_y, change_x, change_y, rayon, color):
    self.x = position_x
    self.y = position_y
    self.vx = change_x
    self.vy = change_y
    self.rayon = rayon
    self.color = color

        def setup(self):
            pass

        def on_update(self, delta_time: float):
            self.x = self.vx
            self.y = self.vy
            self.x += 3
            self.y += 3
            if self.x < self.r:
                self.x *= -1
            if self.x > SCREEN_WIDTH - self.r:
                self.x *= -1
            if self.y < self.r:
                self.y *= -1
            if self.y > SCREEN_HEIGHT - self.r:
                self.y *= -1

        def on_draw(self):
            arcade.start_render()
            arcade.draw_circle_filled(10,10,20, (255, 54, 34))

def rectangle(self, position_x, position_y, change_x, change_y, width, height, color, angle):
    self.x = position_x
    self.y = position_y
    self.vx = change_x
    self.vy = change_y
    self.width = width
    self.height = height
    self.color = color
    self.angle = angle

    def setup(self):
        pass

    def on_update(self, delta_time: float):
        pass

    def on_draw(self):
        arcade.start_render()
        arcade.draw_rectangle_filled(200, SCREEN_HEIGHT / 2, 30, 60,
                                     arcade.csscolor.pass)

class MyGame(arcade.Window):
    def __init__(self, width, height):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT)
        super().__init__(width, height)
        self.liste.balles = []
        self.liste.rectangles = []

        def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
            if button == arcade.MOUSE_BUTTON_LEFT:
                self.liste.balles.append(balle())
                pass
            if button == arcade.MOUSE_BUTTON_RIGHT:
                self.liste.rectangle.append(rectangle())
                pass

def main():
    my_game = MyGame()
    my_game.setup()

    arcade.run()