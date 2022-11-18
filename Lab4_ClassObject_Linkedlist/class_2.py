class pyramid:
    Baselength = 0
    Basewidth = 0
    Pyramidheight = 0

    def __init__(self, Baselength, Basewidth, Pyramidheight):
        self.Baselength = Baselength
        self.Basewidth = Basewidth
        self.Pyramidheight = Pyramidheight

    def calculate(self):
        self.volume = self.Baselength * self.Basewidth * self.Pyramidheight / 3
        return self.volume


def main():
    py = pyramid(10, 7, 17)
    print(f'pyramid = {py.calculate()}')


if __name__ == "__main__":
    main()