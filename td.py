import arcade
# import random

# use mouse clicks as main control

SW = 960
SH = 540


class Tower(arcade.Sprite):
    def __init__(self, price, field_range):
        super().__init__()
        self.price = price
        self.range = field_range


class AttackTower(Tower):
    def __int__(self, damage, price, field_range):
        super().__init__(price, field_range)


class SupportTower(Tower):
    ""


class Cat(AttackTower):
    ""


class Lion(AttackTower):
    ""


class Tiger(AttackTower):
    ""


class Milk(SupportTower):
    ""


class Litter(SupportTower):
    ""


class CatNip(SupportTower):
    ""


class PlayerTowers(""):
    ""


class Yarn(arcade.Sprite):
    ""


class Regular_Yarn(Yarn):
    ""


class Advanced_Yarn(Yarn):
    ""


class Rat(arcade.Sprite):
    ""


class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        arcade.start_render()


def main():
    MyGame(SW, SH, "Tower Defense")
    arcade.run()


if __name__ == "__main__":
    main()
