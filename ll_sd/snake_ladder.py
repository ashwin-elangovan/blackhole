# Functionality

import random

class SnakeAndLadder:
    def __init__(self):
        self.board = [0] * 100
        self.snakes = {}
        self.ladders = {}

    def set_snake(self, head, tail):
        self.board[head] = -1
        self.snakes[head] = tail

    def set_ladder(self, start, end):
        self.board[start] = 1
        self.ladders[start] = end

    def roll_dice(self):
        return random.randint(1, 6)

    def play(self):
        current_position = 0
        while current_position < 100:
            dice_value = self.roll_dice()
            print("You rolled a", dice_value)
            current_position += dice_value
            if current_position >= 100:
                print("You won!")
                break

            if current_position in self.snakes:
                print("Oh no! You landed on a snake. Go to", self.snakes[current_position])
                current_position = self.snakes[current_position]
            elif current_position in self.ladders:
                print("Hurray! You landed on a ladder. Climb to", self.ladders[current_position])
                current_position = self.ladders[current_position]
            else:
                print("You are now at", current_position)

        if current_position >= 100:
            print("Game Over. You won!")
        else:
            print("Game Over. You lost!")


# Create an instance of the game
game = SnakeAndLadder()

# Set snakes
game.set_snake(16, 6)
game.set_snake(48, 26)
game.set_snake(49, 11)
game.set_snake(56, 53)
game.set_snake(62, 19)
game.set_snake(64, 60)
game.set_snake(87, 24)
game.set_snake(93, 73)
game.set_snake(95, 75)
game.set_snake(98, 78)

# Set ladders
game.set_ladder(1, 38)
game.set_ladder(4, 14)
game.set_ladder(9, 31)
game.set_ladder(21, 42)
game.set_ladder(28, 84)
game.set_ladder(36, 44)
game.set_ladder(51, 67)
game.set_ladder(71, 91)
game.set_ladder(80, 100)

# Start the game
game.play()


##########


# Design:

from abc import ABC, abstractmethod
from random import randint

# Abstract class for Tiles
class Tile(ABC):
    def __init__(self, position):
        self.position = position

    @abstractmethod
    def land_on(self):
        pass

# Concrete class for Normal Tiles
class NormalTile(Tile):
    def __init__(self, position):
        super().__init__(position)

    def land_on(self):
        print(f"You landed on a normal tile at position {self.position}")

# Abstract class for Special Tiles
class SpecialTile(Tile):
    def __init__(self, position, destination):
        super().__init__(position)
        self.destination = destination

    @abstractmethod
    def land_on(self):
        pass

# Concrete class for Snake Tiles
class SnakeTile(SpecialTile):
    def __init__(self, position, destination):
        super().__init__(position, destination)

    def land_on(self):
        print(f"Oh no! You landed on a snake at position {self.position}. Go to position {self.destination}")

# Concrete class for Ladder Tiles
class LadderTile(SpecialTile):
    def __init__(self, position, destination):
        super().__init__(position, destination)

    def land_on(self):
        print(f"Hurray! You landed on a ladder at position {self.position}. Climb to position {self.destination}")

# Factory class for creating Tiles
class TileFactory:
    def __init__(self):
        self.tiles = {}

    def add_tile(self, tile):
        self.tiles[tile.position] = tile

    def get_tile(self, position):
        return self.tiles.get(position, NormalTile(position))

# Game class
class SnakeAndLadderGame:
    def __init__(self, tile_factory):
        self.tile_factory = tile_factory
        self.current_position = 0

    def roll_dice(self):
        return randint(1, 6)

    def play(self):
        while self.current_position < 100:
            dice_value = self.roll_dice()
            print(f"You rolled a {dice_value}")
            self.current_position += dice_value
            if self.current_position >= 100:
                print("You won!")
                break

            tile = self.tile_factory.get_tile(self.current_position)
            tile.land_on()
            self.current_position = tile.destination if isinstance(tile, SpecialTile) else self.current_position

        if self.current_position >= 100:
            print("Game Over. You won!")
        else:
            print("Game Over. You lost!")

# Usage
if __name__ == "__main__":
    tile_factory = TileFactory()

    # Add snakes
    tile_factory.add_tile(SnakeTile(16, 6))
    tile_factory.add_tile(SnakeTile(48, 26))
    tile_factory.add_tile(SnakeTile(49, 11))
    tile_factory.add_tile(SnakeTile(56, 53))
    tile_factory.add_tile(SnakeTile(62, 19))
    tile_factory.add_tile(SnakeTile(64, 60))
    tile_factory.add_tile(SnakeTile(87, 24))
    tile_factory.add_tile(SnakeTile(93, 73))
    tile_factory.add_tile(SnakeTile(95, 75))
    tile_factory.add_tile(SnakeTile(98, 78))

    # Add ladders
    tile_factory.add_tile(LadderTile(1, 38))
    tile_factory.add_tile(LadderTile(4, 14))
    tile_factory.add_tile(LadderTile(9, 31))
    tile_factory.add_tile(LadderTile(21, 42))
    tile_factory.add_tile(LadderTile(28, 84))
    tile_factory.add_tile(LadderTile(36, 44))
    tile_factory.add_tile(LadderTile(51, 67))
    tile_factory.add_tile(LadderTile(71, 91))
    tile_factory.add_tile(LadderTile(80, 100))

    # Start the game
    game = SnakeAndLadderGame(tile_factory)
    game.play()
