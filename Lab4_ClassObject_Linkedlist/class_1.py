import math


class cylinders:
    Radius = 0
    Height = 0
    Volume = 0

    def __init__(self, Radius, Height):
        self.Radius = Radius
        self.Height = Height

    def calculate(self):
        self.Volume = math.pi * self.Radius * self.Radius * self.Height
        return self.Volume


def main():
    cy1 = cylinders(5, 10)
    cy2 = cylinders(7, 13)
    print(f'cylinder1 : {cy1.calculate()}')
    print(f'cylinder2 : {cy2.calculate()}')


if __name__ == "__main__":
    main()
