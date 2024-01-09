class Cookie:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color


cookie_one = Cookie("green")
cookie_two = Cookie("blue")

print(f"Cookie one is {cookie_one.get_color()}")
print(f"Cookie one is {cookie_two.get_color()}")

cookie_one.set_color("yellow")

print(f"\nCookie one is now {cookie_one.get_color()}")
print(f"cookie two is still {cookie_two.get_color()}")
