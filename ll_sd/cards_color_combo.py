# Question:
# You have a game and there are combos(consists of cards of 3) in a game which consists of 3 colors. Each player gets 3 cards and each card have value and color. Determine the winner.
# Combos:
# 3 same color
# 3 same value
# etc.

class Card:
    def __init__(self, value, color):
        self.value = value
        self.color = color

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def receive_card(self, card):
        self.hand.append(card)

    def has_color_combo(self):
        # Check if all cards in hand are of the same color
        return len(set(card.color for card in self.hand)) == 1

    def has_value_combo(self):
        # Check if all cards in hand are of the same value
        return len(set(card.value for card in self.hand)) == 1

class Game:
    def __init__(self, players):
        self.players = players

    def determine_winner(self):
        # Determine the winner based on combo rules
        winners = []
        for player in self.players:
            if player.has_color_combo() or player.has_value_combo():
                winners.append(player.name)
        return winners

# Example Usage
if __name__ == "__main__":
    # Creating players
    players = [Player("Alice"), Player("Bob")]

    # Distributing cards
    players[0].receive_card(Card(10, 'red'))
    players[0].receive_card(Card(10, 'red'))
    players[0].receive_card(Card(10, 'red'))

    players[1].receive_card(Card(9, 'blue'))
    players[1].receive_card(Card(10, 'blue'))
    players[1].receive_card(Card(5, 'blue'))

    # Starting the game
    game = Game(players)
    winners = game.determine_winner()

    # Displaying result
    print("Winner(s):", winners)
