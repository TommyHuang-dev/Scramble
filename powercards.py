import random

# LIST OF powercards left
class powercards():
    def __init__(self):
        self.deck = []

        file = open("data/powercards")
        # put all the card values into a 2d list [card, value]
        for line in file:
            cur_type = str(line.split()[0])
            amount = int(file.readline())
            for i in range(amount):
                self.deck.append(cur_type)

    # returns a random list of tiles equal to length num and then subtracts them from the other list
    # the ORDER of return is from 0th list index to nth list index
    def new_card(self):
        draw_index = random.randrange(0, len(self.deck))
        drawn_card = self.deck[draw_index]
        del self.deck[draw_index]
        return drawn_card

    def remove_skips(self, num):
        for i in range(num):
            removeLoc = self.deck.index("skip")
            del self.deck[removeLoc]
