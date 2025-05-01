from random import shuffle

class Card:
    # The strongest suit is the last one, therefore using the greatest index
    suits = ("spades",
            "hearts",
            "diamonds",
            "clubs")
    
    # The first two values are none so that the index matches the number
    # ex. values[2] will be = 2. If we don't do this, then values[2]
    # would be = 4
    values = (None, None, "2", "3", "4", "5", "6", "7", "8", 
              "9", "10", "Jack", "Queen", "King", "Ace")
    
    # Initialize object cardd with two instance variables, suit and value
    def __init__(self, v, s):
        """ suit + value are ints"""
        self.suit = s
        self.value = v

    # Method "less than" used to compare two cards.
    # The reason they're defined as magic methods is so that we can
    # simply use Python's "card1 < card2" instead of manually calling the methods
    # like card1.lt(card2)
    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        return False
    
    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        return False
    
    def __repr__(self):
        v = self.values[self.value] + " of " + self.suits[self.suit]
        return v

class Deck:
    def __init__(self):
        # Create a list of cards
        self.cards = []
        # Create a deck of all 52 cards, append them to the list and shuffle
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i, j))
        shuffle(self.cards)
    
    def rm_card(self):
        # If the deck is empty, return None
        if len(self.cards) == 0:
            return
        # .pop() removes the last element of a list and returns it
        return self.cards.pop()
    
class Player:
    def __init__(self, name):
        self.wins = 0
        self.card = None
        self.name = name

class Game:
    # Ask for two player names, create two players and a deck of cards
    def __init__(self):
        name1 = input("p1 name: ")
        name2 = input("p2 name: ")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)
    
    # Print who won this round
    def wins(self, winner):
        w = "{} wins this round"
        w = w.format(winner)
        print(w)
    
    # Print what card each player drew
    def draw(self, p1n, p1c, p2n, p2c):
        d = "{} drew {} {} drew {}"
        d = d.format(p1n, p1c, p2n, p2c)
        print(d)

    # Method to start the game
    def play_game(self):
        # Assign the previously created deck of cards to the variable "cards"
        cards = self.deck.cards
        print("Beginning War!")
        # Play the game while there are more than 2 cards in the deck
        while len(cards) >= 2:
            m = "q to quit. Any key to play "
            response = input(m)
            # Quit if the player types q
            if response == 'q':
                break
            # p1c = player 1's card, remove one card from the deck for player1
            p1c = self.deck.rm_card()
            # p2c = player 2's card, remove one card from the deck for player 2
            p2c = self.deck.rm_card()
            # self.p1 is a Player object created earlier. Get his name and assign it to p1n
            p1n = self.p1.name
            # self.p2 is a Player object created earlier. Get his name and assign it to p2n
            p2n = self.p2.name
            # display the drawn cards by calling the draw method
            self.draw(p1n, p1c, p2n, p2c)
            
            if p1c > p2c:
                # Increment the wins counter of the winning player (if p1 > p2)
                self.p1.wins += 1
                # Print who won the round
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)
        
        win = self.winner(self.p1, self.p2)
        print("War is over. {} wins".format(win))

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return "It was a tie"
    
game = Game()
game.play_game()
