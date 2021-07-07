

class HaverSacks:
    def __init__(self):
        self.data = None
        self.colors = None

    def loadFile(self):
        with open('input_original.txt') as content:
            self.data = content.readlines()
            self.data = [ line.strip() for line in self.data ]


    def getNumBags(self, color):
        lines = [ line for line in self.data if color in line and line.index(color) != 0 ]
        print(f'lines: {lines}')
        allColors = []

        if len(lines) == 0:
            return []
        else:
            self.colors = [ line[:line.index('bags')] for line in lines ]
            self.colors = [ color for color in self.colors if color not in allColors ]
            print(f'self.colors[] = {self.colors}')
            for color in self.colors:
                allColors.append(color)
                bags = self.getNumBags(color)
                print(f'bags in colors[]: {bags}')

                allColors += bags
                print(f'allColors::: {allColors}')

            uniqueColors = []
            for color in allColors:
                if color not in uniqueColors:
                    uniqueColors.append(color)
                    print(f'uniqueColors len()::: {len(uniqueColors)}')

            return uniqueColors


if __name__ == '__main__':
    my_bag = HaverSacks()
    my_bag.loadFile()
    number_colors = my_bag.getNumBags('shiny gold')
    print(f'Sol::: {len(number_colors)}')



"""
Sol: 242
"""
