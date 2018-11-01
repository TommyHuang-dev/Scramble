## Player class

from random import randint


class player:
    def __init__(self, player_num, num_players, team):  ## Team can be blue or green, game class governs all inputs
        self.player_num = player_num  ## valid numbers 1-6
        self.num_players = num_players ## valid numbers 4 or 6
        self.guess = self.player_num ## make first guess at teammate
        while self.player_num == self.guess:
            self.guess = randint(1, num_players)
        self.team = team
        self.points = 50
        self.cards = ["skip"]
        self.knowns = dict() ## keeps track of known team values

    def change_points(self, num):  ## Update points
        self.points += num

    def get_points(self): ## Return points
        return self.points

    def get_team(self): ## Return team
        return self.team

    def set_team_swap(self, team, player_num): ## Governs team swapping
        if player_num in self.knowns.keys():
            del self.knowns[player_num]
        if team == self.team:
            self.knowns.update(player_num = True)
        else:
            self.knowns.update(player_num = False)
        self.team = team

    def set_team_chaos(self, team): ## Resetting teams after chaos card
        self.knowns.clear()
        self.team = team

    def peek_decision(self, given_card):  ## Governs peeking behaviour, returns player number or 0 if it doesn't want to use
        for value in self.knowns.values(): ## Checks if teammate is already known
            if value == True:
                if given_card:
                    self.cards.append("peek")
                return 0
        to_peek = self.guess
        if not given_card: ## Figures out if it has a peek card stored and if it should be played
            if not "peek" in self.cards:
                return 0
            self.cards.remove("peek")
        while (to_peek == self.guess) or (to_peek == self.player_num): ## Finds person to look at based on door game thing
            to_peek = randint(1, self.num_players)
        return to_peek

    def get_peek(self, to_peek, boolean): ## Governs the result of a peek
        if boolean == True:
            self.guess = to_peek
            self.knowns[to_peek] = True
        else: ## Switches guess if necessary based on door game thing
            self.knowns[to_peek] = False
            temp = to_peek
            if len(self.knowns) == 1:
                while to_peek == temp or to_peek == self.guess or to_peek == self.player_num:
                    to_peek = randint(1, self.num_players)
                self.guess = to_peek
            else: ## This does nothing and will always do nothing, it just points out that there should be nothing
                pass

    def use_skip(self):  ## Decides if a skip should be used, returns True or False
        pass

    def swap_decition(self):
        pass

    def get_swap(self):
        pass

# dude = player(1, 4, "blue")
# print(dude.player_num, dude.num_players, dude.points, dude.cards, dude.guess, dude.knowns)
# if dude.peek_decision(True):
#     dude.get_peek(4, True)
# print(dude.cards, dude.guess, dude.knowns)
# dude.cards.append("peek")
# dude.knowns.clear()
# print(dude.cards)
# print(dude.peek_decision(True))
# print(dude.cards)