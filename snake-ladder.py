import time
import random
import sys

# Board Size
max_steps = 100

class player:
    def __init__(self,name):
        self.won = False
        self.player_name = name
        self.player_position = 0

    def setPosition(self, player_position):
        self.player_position = player_position

    def getPosition(self):
        return self.player_position


class game:
    number_of_players = 0
    player_names = None
    number_of_ladders = 0
    number_of_snakes = 0
    snakes = None
    ladders = None
    number_of_dice = 1
    leaderboard = None

    def __init__(self):
        self.board()
        self.set_players()
        self.got_snakes()
        self.got_ladders()
        self.genratefst() 
        self.leaderboard = []

    def board(self):
        self.board_size = max_steps
        self.board = list(range(1,self.board_size + 1))

    def set_players(self):
        number_of_players = int(input("Enter players count (it should be more then 1 and less then 5): "))
        self.number_of_players = number_of_players
        player_names = []
        for i in range(number_of_players):
            player_name = input(f"Enter player {i +1} name: ")
            player_names.append(player(player_name))
        self.player_names = player_names

    def dice_roll(self):
        dice_roll = [random.randint(1,6) for _ in range(self.number_of_dice)]
        return dice_roll

    def extra_move(self, dice_roll):
        return all([r == 6 for r in dice_roll])

    def got_snakes(self):
        snakes = []
        numberOfSnakes = {
            12: 2,
            18: 4,
            37: 7,
            54: 16,
            60: 23,
            83: 45,
            89: 32,
            92: 25,
            97: 87,
            99: 11
        }
        self.snakes = snakes
        self.numberOfSnakes = numberOfSnakes

    def got_ladders(self):
        ladders = []
        numberOfLadders = {
            4: 19,
            10: 28,
            15: 31,
            21: 69,
            49: 67,
            61: 78,
            73: 86,
            81: 98,
            7: 91
        }
        self.ladders = ladders
        self.numberOfLadders = numberOfLadders

    def play_move(self, k, dice_face):
        player = self.player_names[k]
        print(f"Player {player.player_name} is at {player.player_position}")
        print("Dice rolls: ", dice_face)
        value = player.player_position + sum(dice_face)
        if value > self.board_size:
            return False
        if value == self.board_size:
            print("woohoo game Finish !!!!!!! & Stats are - ")
            return True
        while self.fst[value] != value:
            value = self.fst[value]
            print(value, self.fst[value])
        player.player_position = value
        print(f"Player {player.player_name} reaches to {player.player_position}")
        return False

    def genratefst(self):
        self.fst = {x : x for x in self.board}
        for snake in self.snakes:
            self.fst[snake[0]] = snake[1]
        for ladder in self.ladders:
            self.fst[ladder[0]] = ladder[1]
    
    def start_game(self):
        k = 0
        while True:
            preceding_position = self.player_names[k].player_position
            six_count, turn = 0, True
            while turn:
                turn = False
                print(f"Its {self.player_names[k].player_position} turn")
                input("Hit enter to roll a dice: ")
                dice_face = self.dice_roll()
                if self.play_move(k, dice_face):
                    print(f"{self.player_names[k].player_position} has won the game")
                    self.leaderboard.append(self.player_names[k].player_name)
                    del self.player_names[k]
                    k -= 1
                    if len(self.player_names) == 1:
                        self.leaderboard.append(self.player_names[0].player_name)
                        print("Final positions:")
                        print([(i + 1, v)
                               for i, v in enumerate(self.leaderboard)])
                        return
                    break

                if self.extra_move(dice_face):
                    turn = True
                    six_count += 1

                if six_count == 3:
                    self.player_names[k].player_position = preceding_position
                    print("ohh noo six'es are vanished")
                    break

            k = (k + 1) % len(self.player_names)


if __name__ == '__main__':
    gameStart = game()
    gameStart.start_game()
                    
                    
                        

                    

        
            
            
        

    



        
        


        
        
        

    
    