from random import shuffle

class Card(object):
    suits = ["Spades",
             "Hearts",
             "Diamonds",
             "Clubs"]

    values = [None, None, "2", "3",
             "4", "5", "6", "7",
             "8", "9", "10",
             "Jack", "Queen",
             "King", "Ace"]

    def __init__(self, value, suit):
        """suit + value are ints"""
        self.value = value
        self.suit = suit

    # Overloading the __lt__ magic method.
    # Compares self to a second card object being passed as a parameter.
    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        return False

    # As above, overloading the __gt__ magic method to check if self is
    # greater than a second card object being passed as a parameter.
    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        return False

    def __repr__(self):
        v = self.values[self.value] + " of " + self.suits[self.suit]
        return v

class Deck(object):

    def __init__(self):
        # using list comprehension
        self.cards = [Card(value, suit) for value in range(2, 15) \
                      for suit in range(4)]

        # using nested loops
        #self.cards = []
        #for value in range(2, 15):
        #    for suit in range(4):
        #        self.cards.append(Card(value, suit))
        shuffle(self.cards)

    def rm_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()

class Player(object):

    def __init__(self, name):
        self.name = name
        self.score = 0
        self.card = None

    # Overloading the __repr__ magic method is necessary to return
    # a string with player name. Otherwise, __repr__ returns a Player object.
    #
    # stan = Player("Stan")
    #
    # e.g. (with __repr__ not overloaded):
    # print(stan) ==> <cardgame_war.Player object at 0x10881fa58>
    #
    # e.g. (with __repr__ overloaded per below):
    # print(stan)
    # print(stan.__repr__())
    # stan
    # ALL THREE of the above will print:
    # Player Name: Stan

    def __repr__(self):
        # returns a string instead of a Player object
        return "Player Name: {}".format(self.name)

class Game(object):

    def __init__(self):
        name1 = input("Enter a name for Player 1: ")
        name2 = input("Enter a name for Player 2: ")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    def wins(self, winner):
        print("{} wins this round.\n".format(winner))

    def show_score(self, p1n, p1s, p2n, p2s):
        print("{}: {}\t\t\t{}: {}\n".format(p1n, p1s, p2n, p2s))

    def draw(self, p1n, p1c, p2n, p2c):
        print("{} drew a {}. {} drew a {}.\n".format(p1n, p1c, p2n, p2c))

    def play_game(self):
        cards = self.deck.cards
        print("Beginning War!")
        while len(cards) >= 2:
            m = "q to quit. Any " + "key to play:"
            response = input(m)
            if response == "q":
                break
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            p1n = self.p1.name
            p2n = self.p2.name
            self.draw(p1n, p1c, p2n, p2c)
            if p1c > p2c:
                self.p1.score += 1
                self.wins(self.p1.name)
            else:
                self.p2.score += 1
                self.wins(self.p2.name)
            self.show_score(self.p1.name, self.p1.score, self.p2.name, self.p2.score)

        winner_name = self.winner(self.p1, self.p2)

        print("War is over.")
        if winner_name != "It was a tie!":
            print("{} wins!".format(winner_name))
        else:
            print(winner_name)

    def winner(self, p1, p2):
        if p1.score > p2.score:
            return p1.name
        if p1.score < p2.score:
            return p2.name
        return "It was a tie!"

if __name__ == "__main__":
    game = Game()
    game.play_game()
