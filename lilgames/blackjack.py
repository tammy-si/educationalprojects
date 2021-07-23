# blackjack card game with Python 3.8.10. There's betting, but there is no split option and no insurance.
# goal here is to try learn and get more comfortable with object oriented programming
# watched Executed Binary's Python OOP - Deck of Cards as a starting point/influence
import random
import keyboard
import sys

# class for a single card
class Card:
    # each card should have it's own suit and value
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.tval =  self.tval(value)

    # showCard method of card should be to display the card's suit and value
    def showCard(self):
        map = {1: "Ace", 11: "Jack", 12: "Queen", 13: "King"}
        if self.value in [1, 11, 12, 13]:
            value = map[self.value]
        else:
            value = self.value
        print( "{} of {} ".format(value, self.suit))

    def tval(self, value):
    # method to get the actual values of the cards
        dict_vals = {}
        for i in range(1, 14):
            if i == 1:
                dict_vals[i] = 11
            elif i > 10:
                dict_vals[i] = 10
            else:
                dict_vals[i] = i
        return dict_vals[value]

# Deck class
class Deck:
    # all cards are kept in a list called self.cards where self is an instance of Deck class
    def __init__(self):
        self.cards = []
        self.buildDeck()

    # buildDeck is to populate the cards list with all 52 Cards objects/instances (Note: called when deck is first made)
    def buildDeck(self):
        for v in range(1,14):
            for s in ["Clubs (♣)", "Diamonds (♦)", "Hearts (♥)", "Spades (♠)"]:
                self.cards.append(Card(v, s))

    # show what cards are currently in the deck
    def showDeck(self):
        print(str(len(self.cards)) + " cards in the deck.")
        for card in self.cards:
            card.showCard()

    def shuffle(self):
        # Fisher yates shuffling algorithm. We start from the back. We go from index 51 to 1 cause the last index/card is 0 and doesn't need to be swapped.
        for i in range(len(self.cards) - 1, 0, -1):
            # we pick random index from 0 to i and then swap the current card we're at with the random index card
            j = random.randint(0, i + 1)
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]

    # draw a single card from the top of the deck
    def drawCard(self):
        return self.cards.pop()

# class for the people such as the dealer or the player
class Person:
    # each person should have a hand, which will later be populated by cards drawn from the deck
    def __init__(self, name):
        self.hand = []
        self.name = name
        self.handtotal = 0
    
    # player and dealers draw cards from the deck. We have to pass in a deck object so that we have something to draw from.
    def draw(self, deckers):
        self.hand.append(deckers.drawCard())

    # show what cards are in the person's hand
    def showHand(self):
        print(f"{self.name}'s hand: ")
        for card in self.hand:
            if type(card) == str:
                print("hidden")
            else:
                card.showCard()
        print()

    # to check whether the player or dealer has gotten a natural blackjack
    def blackjack(self):
        if self.hand[0] == "hidden":
            self.hand[0] = self.hidden
        if self.hand[0].tval + self.hand[1].tval == 21:
            return True

    # total value of either the players or dealer's hands
    def calcHandtotal(self):
        self.handtotal = 0
        for i in range(len(self.hand)):
            if self.hand[i] == "hidden":
                self.hand[i] = self.hidden
        for card in self.hand:
            self.handtotal += card.tval
        
        # to handle aces values and make sure the value of the ace switches between 1 and 11 depending on whether it'd help the hand
        while self.handtotal > 21:
            for j in range(len(self.hand)):
                # look through the hand for aces, and then if there ace that isn't counted as 1 instead of 11 yet, we change it then stop the search
                if self.hand[j].value == 1 and self.hand[j].tval != 1:
                    self.hand[j].tval = 1
                    break
            break
        # recalculate incase the ace value changed and effected the handtotal
        self.handtotal = 0
        for card in self.hand:
            self.handtotal += card.tval
        return self.handtotal

    # to empty the hand and play another round
    def discardHand(self):
        self.hand = []

class Player(Person):
    def __init__(self, name):
        super().__init__(name)
        self.money = 1000
        self.bet_amount = None
        self.highest = self.money

    def placeBet(self):
        try:
            bet_amount = int(input(f"Hi {self.name}! You currently have ${self.money}. How much do you want to bet? "))
            if 0 < bet_amount <= self.money:
                self.bet_amount = bet_amount
                return True
            else:
                print("An error has occured. Make sure you have an integer greater than 0 and you enough money to bet.")
        except:
            print("An error has occured. Make sure you have an integer greater than 0 and you enough money to bet.")

    # at the end of play we sort of either take away money from the player if they lost, or if they won, the house pays up 
    def cashout(self, type):
        if type == "blackjack":
            print("Blackjack! \n")
            self.money += 1.5 * self.bet_amount
            if self.money > self.highest:
                self.highest = self.money
        elif type == "lose":
            print("You lost :( \n")
            self.money -= self.bet_amount
        elif type == "win":
            print("You won :) \n")
            self.money += self.bet_amount
            if self.money > self.highest:
                self.highest = self.money
    
    def getChoice(self):
        choice = ""
        if self.bet_amount <= (self.money / 2) and len(self.hand) == 2:
            while choice not in ["hit", "double", "stand"]:
                choice = input("Do you want to hit, double or stand? ").lower()
            return choice
        while choice not in ["hit", "stand"]:    
            choice = input("Do you want to hit or stand? ").lower()
        return choice


# dealer sub class that inherits from the superclass Person
class Dealer(Person):
    # the self.hidden is to temporarily hold the 1st card that the dealer draws
    def __init__(self):
        super().__init__("Dealer")
        self.hidden = ""
        
    # like a normal draw but it's hidden because in blackjack the dealer's 1st card is hidden. The string "hidden" is put into the dealer's hand as a placeholder.
    #  We remember what card the hidden card by storing the card object in self.hidden
    def hiddenDraw(self, deck):
        self.hidden = deck.drawCard()
        self.hand.append("hidden")

def showHands(p, d):
    p.showHand()
    d.showHand()

def discardHands(p, d):
    p.discardHand()
    d.discardHand()

def game():
    # make and shuffle the original 52 card deck
    deck = Deck()
    deck.shuffle()

    dealer = Dealer()
    player = Player(input("What's your name? "))
    while player.money > 0:
        cashedout = False
        # before anything happens the player has to say how much they want to bet. Only continue when the bet is succesfully made
        while True:
            if player.placeBet():
                break
        # once you place the bets you can start dealing out the first 4 cards.
        player.draw(deck)
        dealer.hiddenDraw(deck)
        player.draw(deck)
        dealer.draw(deck)
        showHands(player, dealer)

        # check if the player and dealer both got a natural blackjack if they did then you push
        if player.blackjack() and dealer.blackjack():
            dealer.calcHandtotal()
            showHands(player, dealer)
            discardHands(player, dealer)
            print("Push")
            continue
        # if the player gets a blackjack and we check that the dealer didn't, then we cashout for the player
        elif player.blackjack() and not dealer.blackjack():
            print(f"{player.name} got a blackjack!")
            dealer.calcHandtotal()
            showHands(player, dealer)
            discardHands(player, dealer)
            player.cashout("blackjack")
            continue

        # entire player turn
        while True:
            choice = player.getChoice()
            player.calcHandtotal()
            if choice == "hit":
                player.draw(deck)
                showHands(player, dealer)
            elif choice == "double":
                player.bet_amount *= 2
                player.draw(deck)
                showHands(player, dealer)
                
            player.calcHandtotal()
            if player.handtotal == 21:
                break
            elif player.handtotal > 21:
                dealer.calcHandtotal()
                showHands(player, dealer)
                print("Bust")
                player.cashout("lose")
                cashedout = True
                break

            if choice == "stand":
                showHands(player, dealer)
                break
            if choice == "double":
                break
        
        dealer.calcHandtotal()
        # dealer turn
        while dealer.handtotal < 17 and cashedout == False:
            dealer.draw(deck)
            showHands(player, dealer)
            dealer.calcHandtotal()
            # dealer bust after drawing a new card
            if dealer.handtotal > 21:
                print("Dealer bust")
                player.cashout("win")
                cashedout = True
                break

        # find the winner
        # if player and dealer equal push and don't take or get any 
        player.calcHandtotal()
        dealer.calcHandtotal()
        if player.handtotal == dealer.handtotal and cashedout == False:
            # just in case we have a case where player gets 21, but dealer gets a natural blackjack, dealer wins in this case even though they both technically have 21
            if dealer.blackjack():
                showHands(player, dealer)
                discardHands(player, dealer)
                player.cashout("lose")
                continue
            print("Push")
            showHands(player, dealer)
            discardHands(player, dealer)
            continue
        # if the player is closer to 21 than the dealer, then the player wins
        elif player.handtotal > dealer.handtotal and cashedout == False:
            showHands(player, dealer)
            discardHands(player, dealer)
            player.cashout("win")
            continue
        # if the dealer is closer to 21 than the player, then the house wins
        elif player.handtotal < dealer.handtotal and cashedout == False:
            showHands(player, dealer)
            discardHands(player, dealer)
            player.cashout("lose")
            continue
        discardHands(player, dealer)

        # make sure we don't run out of cards
        if (len(deck.cards) <= 15):
            print("Adding old cards back into the deck and shuffling.")
            deck.cards = []
            deck.buildDeck()
            deck.shuffle()

    print("You've run out of money :(. Your highest bank amount was $" + str(player.highest))
    print("If you want to play again, press p. If you want to quit, press q.")
    
    # replaying and closing
    while True:
        if keyboard.read_key() == "p":
            game()
        elif keyboard.is_pressed("q"):
            sys.exit()

game()

