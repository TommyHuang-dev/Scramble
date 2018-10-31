import random

# hi
# LIST OF TILES + start and end tile
# in tiles file:
# type (e.g. get)
# value (e.g. 10)
# quantity (e.g. 3)

# TILES CLASS
# functions: get a new tile
class tiles():
    def __init__(self):
        self.deck = []

        self.c_size = 0  # current length

        file = open("data/tiles")
        # put all the card values into a 2d list [card, value]
        for line in file:
            cur_type = str(line.split()[0])
            val = int(file.readline())
            amount = int(file.readline())
            for i in range(amount):
                self.deck.append([cur_type, val])
            self.c_size += amount

        self.o_size = self.c_size + 1  # original size

    # returns a random list of tiles equal to length num and then subtracts them from the other list
    # the ORDER of return is from 0th list index to nth list index
    def new_tile(self, num):
        result = []
        for i in range(num):
            if self.o_size == self.c_size + 1:  # start tile
                result.append(["start", 0])
                self.c_size -= 1
            elif self.c_size == 0:  # end tile
                result.append(["end", 2])
                return result
            else:  # random tile
                choice = random.randrange(0, len(self.deck))
                result.append(self.deck[choice].copy())
                del(self.deck[choice])

                self.c_size -= 1

        return result

hi = tiles()
print(hi.new_tile(5))
print(hi.new_tile(3))
print(hi.new_tile(30))