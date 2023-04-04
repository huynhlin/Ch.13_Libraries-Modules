import arcade
# import random

# use mouse clicks as main control

# thingg i want to implement
# pause screen with timescale + slide graphics
# challenging modes
# drag and drop
# "pop" count
# tower that scales infinitely with pops, for endgame
# unrelated but some kind of surfing/skateboarding game would be a cool final too
# png for "track"
# bg music?
# skins ?
# png overlay for the trim and stuff


SW = 960
SH = 540

#
# class Tower(arcade.Sprite):
#     def __init__(self, price, field_range, speed, damage):
#         super().__init__()
#         self.price = price
#         self.range = field_range
#         self.speed = speed
#         self.damage = damage
#         self.upgrades = {"Name": "",
#                          "Price": 0,
#                          "Boost": ""}, \
#                         {"Name": "",
#                          "Price": 0,
#                          "Boost": ""}, \
#                         {"Name": "",
#                          "Price": 0,
#                          "Boost": ""}
#
#
# class AttackTower(Tower):
#     def __init__(self, price, field_range, attack_speed, damage):
#         super().__init__(price, field_range, attack_speed, damage)
#         self.price = price
#         self.field_range = field_range
#         self.attack_speed = attack_speed
#         self.damage = damage
#         self.textures = []
#
# class SupportTower(Tower):
#     ""
#
#
# class Cat(AttackTower):
#     ""
#
#
# class Lion(AttackTower):
#     ""
#
#
# class Tiger(AttackTower):
#     ""
#
#
# class Milk(SupportTower):
#     ""
#
#
# class Litter(SupportTower):
#     ""
#
#
# class CatNip(SupportTower):
#     ""
#
#
# class PlayerTowers(""):
#     ""
#
#
# class Yarn(arcade.Sprite):
#     ""
#
#
# class Regular_Yarn(Yarn):
#     ""
#
#
# class Advanced_Yarn(Yarn):
#     ""
#
#
# class Rat(arcade.Sprite):
#     ""


class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        arcade.start_render()
        border_length = 10
        arcade.draw_rectangle_outline(SW - 64 - border_length, SH/2, 128 + border_length,
                                      SH - border_length, arcade.color.RED, border_length)
        arcade.draw_line((SW - (64 - border_length)/2), SH, SW - ((64 - border_length)/2), 0, arcade.color.RED,
                         border_length)


def main():
    MyGame(SW, SH, "Tower Defense")
    arcade.run()


if __name__ == "__main__":
    main()
