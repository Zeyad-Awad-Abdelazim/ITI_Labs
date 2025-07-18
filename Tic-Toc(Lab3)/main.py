import os
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# Players Entity Class
class Player:
    def __init__(self):
        self.name = ""
        self.symbol = ""

    def set_name(self):
        while True:
            name = input("Enter Your Name: ")
            if name.isalpha(): 
                self.name = name
                break
            else: print("Invalid Name! only letters are allowed.")

    def choose_symbol(self):
       while True: 
            symbol = input(f"hey {self.name}, choose a symbol (single letter): ")
            if symbol.isalpha() and len(symbol) == 1:
               self.symbol = symbol
               break
            else: print("Invalid Symbol! Choose only a single letter.")

# Menus Entity Class
class Menu:
    def display_main_menu(self):
        mainMenu = """
        ######################################
        ###### Welcome to Tic-Toc Game #######
        ######################################
        ###### 1. Start a New Game.    #######
        ###### 2. Quit.                 #######
        ######################################
        """
        choice = int(input(f"{mainMenu} \n Enter Your Choice: "))
        while True:
            if choice == 1 or choice == 2:
                break
            else:
                choice = input("Please Enter 1 or 2: ")
        return choice
    
    def display_endGame_menu(self):
        endGameMenu = """
        //////////////////////////////
        //////// Game Over ! ////////
        ////////////////////////////
        /////// 1. Restart.  //////
        /////// 2. Quit.    //////
        /////////////////////////
        """
        choice = int(input(f"{endGameMenu} \n Enter Your Choice: "))
        while True:
            if choice == 1 or choice == 2:
                break
            else:
                choice = input("Please Enter 1 or 2: ")
        return choice

# Board Entity Class
class Board:
    def __init__(self):
        self.board = [str(i) for i in range(1,10)] #1,2,3,4,...,8,9

    def display_board(self):
        for i in range(0, 9, 3):
            print("|".join(self.board[i:i+3]))
            if i < 6:
                print("-" * 5)

    def update_move(self, choice, symbol):
        if not self.check_is_valid_move(choice):
            self.board[choice-1] = symbol
            return True
        
        return False
        
    def check_is_valid_move(self, moveChoice):
        return self.board[moveChoice-1].isdigit()
    
    def reset_board(self):
        self.board = [str(i) for i in range(1,10)] #1,2,3,4,...,8,9


# Main Game Class
class Game:
    def __init__(self):
        self.players = [Player(), Player()]
        self.board = Board()
        self.menu = Menu()
        self.player_index = 0

    def start_game(self):
        choice = self.menu.display_main_menu()
        if choice == 1:
            self.setup_players()
            self.initialize_game()
        else:
            self.quit_game()

    def setup_players(self):
        for number, player in enumerate(self.players, start=1):
            print(f"Player {number}, Enter your details: ")
            player.set_name()
            player.choose_symbol()
            print("-"*40)


    def initialize_game(self):
        while True:
            self.play_turn()
            if self.check_win() or self.check_draw():
                choice = self.menu.display_endGame_menu()
                if choice == 1:
                    self.restart_game()
                else:
                    self.quit_game()
                    break
            

    def quit_game(self):
        print("Game Endend.")

    def play_turn(self):
        player = self.players[self.player_index]
        self.board.display_board()
        print(f"{player.name}'s turn ({player.symbol})")
        while True:
            try:
                cell_choice = int(input("Enter your cell choice (1 -> 9): "))
                if 1 <= cell_choice <=9 and self.board.update_move(cell_choice, player.symbol):
                    break
                else:
                    print("Invalid move, try again ...")
            except ValueError:
                print("Enter a number between 1 & 9")
        self.switchPlayer()
        
    def check_win(self):
        winArr = [
            [0,1,2], [3,4,5], [6,7,8], #rows
            [0,3,6], [1,4,7], [2,5,8], #columns
            [0,4,8], [2,4,6]           #diagonals
        ]
        for i in winArr:
            if self.board.board[i[0]] == self.board.board[i[1]] == self.board.board[i[2]]:
                return True
            else: 
                return False

    def check_draw(self):
        return all(not cell.isdigit() for cell in self.board.board)

    def restart_game(self):
        self.board.reset_board()
        self.player_index = 0
        self.initialize_game()

    def switchPlayer(self):
        self.player_index = 1 - self.player_index

game = Game()
game.start_game()