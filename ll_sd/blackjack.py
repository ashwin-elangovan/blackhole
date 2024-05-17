# Setup:
# Players place their bets.
# The dealer deals two cards face up to each player, including themselves.
# Gameplay:
# Players take turns deciding whether to "hit" (take another card) or "stand" (keep their current hand).
# Players can also have additional options like "splitting" pairs, "doubling down" on certain hands, or taking "insurance" against the dealer getting Blackjack.
# Dealer's Turn:
# After all players have completed their turns, the dealer reveals their facedown card.
# The dealer must hit until their hand total is 17 or higher.
# Outcome:
# If a player's hand exceeds 21, they "bust" and lose their bet.
# If a player's hand total is closer to 21 than the dealer's hand without going over 21, they win and receive a payout.
# If the player's hand ties with the dealer's hand, it's a "push," and the player neither wins nor loses.
# If the dealer busts, all remaining players win.
# If the dealer's hand total is closer to 21 than the player's hand total, the player loses their bet.
# Blackjack:
# If a player is dealt an Ace and a card with a value of 10 (10, Jack, Queen, or King) as their initial two cards, they have a "Blackjack" and typically win 1.5 times their bet unless the dealer also has Blackjack, resulting in a push.
# Next Round:
# After the outcome is determined, players can place new bets and start a new round.


import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = self.get_value()

    def get_value(self):
        if self.rank in ['J', 'Q', 'K']:
            return 10
        elif self.rank == 'A':
            return 11  # Ace can be 1 or 11
        else:
            return int(self.rank)

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades']:
            for rank in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += card.value
        if card.rank == 'A':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class Player(Hand):
    def __init__(self, name, bankroll):
        super().__init__()
        self.name = name
        self.bankroll = bankroll

    def place_bet(self, bet):
        if bet > self.bankroll:
            print("Insufficient funds. Please enter a lower bet.")
            return False
        self.bankroll -= bet
        return bet

    def first_win(self, bet):
        self.bankroll += bet * 1.5

    def win(self, bet):
        self.bankroll += bet * 2

    def push(self, bet):
        self.bankroll += bet

class Dealer(Hand):
    def __init__(self):
        super().__init__()

    def play(self, deck):
        while self.value < 17:
            self.add_card(deck.deal())
            self.adjust_for_ace()

class Game:
    def __init__(self):
        self.deck = Deck()
        self.player = Player("Player", 1000)
        self.dealer = Dealer()

    def deal_cards(self):
        self.player.add_card(self.deck.deal())
        self.player.add_card(self.deck.deal())
        self.dealer.add_card(self.deck.deal())
        self.dealer.add_card(self.deck.deal())

    def player_turn(self):
        while True:
            choice = input("Hit or Stand? (h/s) ")
            if choice.lower() == 'h':
                self.player.add_card(self.deck.deal())
                self.player.adjust_for_ace()
                print(f"Your hand: {', '.join(str(card) for card in self.player.cards)}")
                print(f"Your hand value: {self.player.value}")
                if self.player.value > 21:
                    print("Bust! You lose.")
                    return
            elif choice.lower() == 's':
                break
            else:
                print("Invalid choice. Please try again.")

    def dealer_turn(self):
        print(f"Dealer's hand: {self.dealer.cards[0]}, ?")
        self.dealer.play(self.deck)
        print(f"Dealer's hand: {', '.join(str(card) for card in self.dealer.cards)}")
        print(f"Dealer's hand value: {self.dealer.value}")

    def determine_winner(self):
        if self.player.value > 21:
            print("You busted! Dealer wins.")
        elif self.dealer.value > 21:
            print("Dealer busted! You win.")
            self.player.push(bet)
        elif self.player.value > self.dealer.value or self.player.value == 21:
            print("You win!")
            self.player.win(bet)
        elif self.player.value < self.dealer.value or self.dealer.value == 21:
            print("Dealer wins.")
        else:
            print("It's a tie! Push.")
            self.player.push(bet)

    def play(self):
        while True:
            print(f"Your bankroll: {self.player.bankroll}")
            bet = self.player.place_bet(int(input("Enter your bet: ")))
            if not bet:
                continue

            self.deck.shuffle()
            self.deal_cards()
            print(f"Your hand: {', '.join(str(card) for card in self.player.cards)}")
            print(f"Dealer's hand: {self.dealer.cards[0]}, ?")

            if self.player.value == 21:
                self.player.first_win()
            else:
                self.player_turn()
                if self.player.value < 21:
                    self.dealer_turn()

                self.determine_winner()

            play_again = input("Play again? (y/n) ")
            if play_again.lower() != 'y':
                print(f"Thanks for playing! Your final bankroll: {self.player.bankroll}")
                break

# Start the game
game = Game()
game.play()
