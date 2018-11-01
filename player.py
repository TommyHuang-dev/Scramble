## Player class

from random import randint


class player:
    def __init__(self, player_num, num_players, team):  ## Team can be blue or green, game class governs all inputs
        self.player_num = player_num  ## valid numbers 1-6
        self.num_players = num_players
        self.guess = self.player_num
        while self.player_num == self.guess:
            self.guess = randint(1, num_players)
        self.team = team
        self.points = 50
        self.cards = ["skip"]
        self.knowns = dict()
        self.unknowns = list()

    def change_points(self, num):  ## Update points

        self.points += num

    def get_points(self):

        return self.points

    def get_team(self):

        return self.team

    def peek_decition(self):  ## Governs peeking behaviour, returns player number or 0 if it doesn't want to use

        for value in self.knowns.values():

            if value == True:
                self.cards.append("peek")

                return 0

        to_peek = self.guess

        while (to_peek == self.guess) or (to_peek == self.num):
            to_peek = randint(1, self.num_players)

        return to_peek

    def get_peek(self, to_peek, boolean):

        if boolean == True:

            self.guess = to_peek

        else:

            pass

            ## FIGURE OUT HOW TO KNOW WHEN TO SWITCH

    def swap(self):  ## Governs swapping behaviour, returns player number

        pass

def use_skip(self):  ## Decides if a skip should be used, returns True or False

    pass