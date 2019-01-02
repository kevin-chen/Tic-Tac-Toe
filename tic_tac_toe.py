# CS-UY 1114
# Final Project
# Kevin Chen

import turtle
import time
import random
import tkinter
import math
import copy

class Board:
    def __init__(self):
        '''
        Sig: Board -> NoneType
        Construct a new blank Board
        '''
        # This list represents the board. It's a list
        # of nine strings, each of which is either
        # "X", "O", "_", representing, respectively,
        # a position occupied by an X, by an O, and
        # an unoccupied position. The first three
        # elements in the list represent the first row,
        # and so on. Initially, all positions are
        # unoccupied.
        self.the_board = [ "_", "_", "_",
                           "_", "_", "_",
                           "_", "_", "_"]
        self.height = turtle.window_height() # 810
        self.width = turtle.window_width() # 840

    def draw_board(self):
        """
        signature: Board -> NoneType
        Given the current state of the game, draws
        the board on the screen, including the
        lines and the X and O pieces at the position
        indicated by the parameter.
        Hint: Write this function first!
        """
        turtle.clear()

        self.height = turtle.window_height() # 810
        self.width = turtle.window_width() # 840

        # Drawing grid
        turtle.pencolor("blue")
        self.draw_line((-self.width/2, self.height/6), (self.width/2, self.height/6), 10) # self.draw_line((-420,135), (420,135), 10)
        self.draw_line((-self.width/2, -self.height/6), (self.width/2, -self.height/6), 10) # self.draw_line((-420,-135), (420,-135), 10)
        turtle.right(90)
        self.draw_line((-self.width/6, self.height/6*3), (-self.width/6, -self.height/6*3), 10) # self.draw_line((-140,405), (-140,-405), 10)
        turtle.right(90)
        self.draw_line((self.width/6, self.height/6*3), (self.width/6, -self.height/6*3), 10) # self.draw_line((140,405), (140,-405), 10)
        turtle.pencolor("red")

        # Placing X, 0
        for i in self.the_board:
            if i == "X":
                self.draw_x()
            elif i == "O":
                self.draw_circle()

        turtle.update()
        
    def draw_line(self, first, second, pensize = 10):
        # Helper
        '''
        Sig: Board, tuple(float, float), tuple(float, float), int -> NoneType
        Just draws a line given two coordinates
        '''
        goTo(first)
        turtle.pensize(pensize)
        turtle.pendown()
        turtle.goto(second)
        turtle.penup()
        turtle.setheading(0)
        turtle.pensize(0)
        
    def draw_circle(self):
        # Helper
        '''
        Sig: Board -> NoneType
        Draws circle based on the board and position
        '''
        curr_board_pos = 0
        for j in range(self.height//6, -self.height//6*3 - 1, -self.height//3): # for j in range(131, -395, -270):
            for i in range(-self.width//3, self.width//3 + 1, self.width//3): # for i in range(-280, 281, 280):
                if self.the_board[curr_board_pos] == "O":
                    goTo((i, j))
                    circle(self.height/6)
                curr_board_pos += 1

    def draw_x(self):
        # Helper
        '''
        Sig: Board -> NoneType
        Draws an X based on the board and positions
        '''
        turtle.pensize(5)
        curr_board_pos = 0

        x1 = -self.width/2 # x1 = -420
        x2 = -self.width//6 # x2 = -140
        y1 = self.height//6*3 # y1 = 393
        y2 = self.height//6 # y2 = 131
        
        for j in range(self.height//6, -self.height//6*3 - 1, -self.height//3): # for j in range(131, -394, -262):
            for i in range(-self.width//6, self.width//2 + 1, self.width//3): # for i in range(-140, 421, 280):
                if self.the_board[curr_board_pos] == "X":
                    self.draw_line((x1, y1), (x2, y2))
                    self.draw_line((x2, y1), (x1, y2))
                x1 += self.width//3 # x1 += 280
                x2 += self.width//3 # x2 += 280
                curr_board_pos += 1
            x1 = -self.width//2 # x1 = -420
            x2 = -self.width//6 # x2 = -140
            y1 -= self.height//3 # y1 -= 262
            y2 -= self.height//3 # y2 -= 262
            
        turtle.pensize(0)
        
class Score:
    def __init__(self, scoreboard, player_wins, computer_wins, round_num):
        '''
        Sig: Score, str, int, int, int -> NoneType
        Constructs a new Score, creates/modifies scoreboard.txt, and opens new scoreboard window
        '''
        # Get the score board file or makes new score board file
        try:
            score_board = open(scoreboard, "r")
            score_board.close()
            score_board = open(scoreboard, "a")
            score_board.write("NEW GAME | ")
            score_board.close()
        except FileNotFoundError:
            score_board = open(scoreboard, "w")
            score_board.write("MASTER SCORE BOARD\nNEW GAME | ")
            score_board.close()

        #Tkinter
        self.root = tkinter.Tk()
        self.root.title("SCORE BOARD")
        self.root.geometry("500x500")

        self.frame = tkinter.Frame(self.root)
        self.frame.pack()

        self.title_label = tkinter.Label(self.frame, text = "Score Board", font="Verdana 28 bold")
        self.title_label.pack()

        self.skip_label = tkinter.Label(self.frame, text = "\n")
        self.skip_label.pack()

        self.entry_label = tkinter.Label(self.frame, text = "Enter your name", font="Verdana 16")
        self.entry_label.pack()
        self.entry = tkinter.Entry(self.frame, font="Verdana 28 bold")
        self.entry.pack()
        self.entry.insert(0, "You")

        self.skip_label = tkinter.Label(self.frame, text = "\n")
        self.skip_label.pack()

        self.player_label = tkinter.Label(self.frame, text = "Player Wins: " + str(player_wins), font="Verdana 16 bold")
        self.player_label.pack()
        self.computer_label = tkinter.Label(self.frame, text = "Computer Wins: " + str(computer_wins), font="Verdana 16 bold")
        self.computer_label.pack()
        self.round_label = tkinter.Label(self.frame, text = "Round: " + str(round_num), font="Verdana 16 bold")
        self.round_label.pack()

        self.skip_label = tkinter.Label(self.frame, text = "\n")
        self.skip_label.pack()

        self.quit_button = tkinter.Button(self.frame, text = "QUIT", fg = "red", font="Verdana 20 bold", command = quit)
        self.quit_button.pack()
        
    def update_score(self, scoreboard, winner, player_wins, computer_wins, round_num):
        # Helper
        '''
        Sig: Score, str, str, int, int, int, NoneType
        Updates the GUI scoreboard and scoreboard.txt
        '''
        score_board = open(scoreboard, "a")
        
        if winner == "O":
            score_board.write("Round: " + str(round_num) + " | " + str(self.entry.get()) + " WINS" + "\n")
        elif winner == "X":
            score_board.write("Round: " + str(round_num) + " | X WINS" + "\n")
        else:
            score_board.write("Round: " + str(round_num) + " | NO WINNER" + "\n")
            
        score_board.write("Player Score: " + str(player_wins) + "\n")
        score_board.write("Computer Score: " + str(computer_wins) + "\n" +"\n")

        round_num += 1

        # GUI Updates
        self.player_label.config(text="Player Wins: " + str(player_wins))
        self.computer_label.config(text="Computer Wins: " + str(computer_wins))
        self.round_label.config(text="Round: " + str(round_num))

        score_board.close()

    def write(self, scoreboard, text):
        # Helper
        '''
        Sig: Score, str, str
        Writes the text in scoreboard.txt
        '''
        score_board = open(scoreboard,"a")
        score_board.write(text)
        score_board.close()
        
    def get_highest_score(self, scoreboard):
        # Helper
        '''
        Sig: Score, str
        Gets the highest score from scoreboard.txt, returns the highest score
        The high score is calculated by getting the difference between player
        score and computer score
        '''
        highscore_player = 0
        highscore_computer = 0
        biggest_difference = 0
        score_board = open(scoreboard,"r")
        score_board.readline() #read 1
        score_board.readline() #read 2
        for player in score_board: #read 3
            player = player.strip()
            computer = score_board.readline() #read 4
            player_score = int(player[player.find(": ")+2:])
            computer_score = int(computer[computer.find(": ")+2:])
            if player_score - computer_score > biggest_difference:
                biggest_difference = player_score - computer_score
            score_board.readline() #read 5
            score_board.readline() #read 6
        score_board.close()
        return biggest_difference
            
class Game:
    def __init__(self):
        '''
        Sig: Game -> NoneType
        Constructs a new Game with blank Board and a simulation (temp) Board
        self.score_board will reinstantiate in later_init
        '''
        self.the_board = Board()
        self.simulate_board = Board()
        self.player_wins = 0
        self.computer_wins = 0
        self.round_num = 1
        self.score_board = 0
        
    def later_init(self):
        # Helper
        '''
        Sig: Game -> NoneType
        Only occurs once in play_game; this is because we have to create a simulate Game object for do_computer_move, 
        but we still need the field variables for the class, so we make a later_init to not trigger create mulitple
        score_board objects and windows for simulations
        '''
        # Turtle Setup
        turtle.setup(840,810, 650, 0)
        turtle.title("TIC-TAC-TOE")
        # turtle.Screen().bgpic("giphy.gif")
        turtle.bgcolor("Misty Rose")
        turtle.pencolor("red")
        turtle.tracer(0,0)
        turtle.hideturtle()
        self.score_board = Score("scoreboard.txt", self.player_wins, self.computer_wins, self.round_num)
        
    def reset(self):
        # Helper
        '''
        Sig: Game -> NoneType
        Resets the board for a new game
        '''
        for i in range(0, len(self.the_board.the_board)):
            self.the_board.the_board[i] = "_"
        time.sleep(1)
        turtle.clear()
        turtle.update()
        self.the_board.draw_board()
        
    def do_user_move(self, x, y):
        """
        signature: Game, int, int -> bool
        Given a list representing the state of the board
        and an x,y screen coordinate pair indicating where
        the user clicked, update the board
        with an O in the corresponding position. Your
        code will need to translate the screen coordinate
        (a pixel position where the user clicked) into the
        corresponding board position (a value between 0 and
        8 inclusive, identifying one of the 9 board positions).
        The function returns a bool indicated if
        the operation was successful: if the user
        clicks on a position that is already occupied
        or outside of the board area, the move is
        invalid, and the function should return False,
        otherwise True.
        """
        # print("user clicked at "+str(x)+","+str(y))
        if -self.the_board.width/2 < x < self.the_board.width/2 and -self.the_board.height//6*3 < y < self.the_board.height//6*3:
            curr_board_pos = 0
            marOfError = 20
            # print("j", self.the_board.height//6, -self.the_board.height//6*3, -(self.the_board.height//6 + self.the_board.height//6*3)//2 + 20)
            # print("i", -self.the_board.width//6, self.the_board.width//2, (self.the_board.width//2 + self.the_board.width//6)//2 - 10)
            for j in range(self.the_board.height//6, -self.the_board.height//6*3, -(self.the_board.height//6 + self.the_board.height//6*3)//2 + marOfError): # has to be before threshold # for j in range(131, -393, -250): 
                for i in range(-self.the_board.width//6, self.the_board.width//2, (self.the_board.width//2 + self.the_board.width//6)//2 - marOfError): # has to be before threshold # for i in range(-140, 420, 270):
                    # print(curr_board_pos)
                    # print("i", i, "j", j)
                    # print(-(self.the_board.height//6 + self.the_board.height//6*3)//2 + 20)
                    # print("j diff", (self.the_board.height//6 + self.the_board.height//6*3)//2, (self.the_board.height//6 + self.the_board.height//6*3)//2 + 20)
                    # print("i diff", (self.the_board.width//2 + self.the_board.width//6)//2, (self.the_board.width//2 + self.the_board.width//6)//2 - 20)
                    if (i - (self.the_board.width//2 + self.the_board.width//6)//2 - marOfError <= x <= i and j + (self.the_board.height//6 + self.the_board.height//6*3)//2 - marOfError >= y >= j) and self.the_board.the_board[curr_board_pos] == "_":
                        self.the_board.the_board[curr_board_pos] = "O"
                        return True
                    curr_board_pos += 1
        return False
    
    def check_row(self):
        # Helper
        '''
        Sig: Game -> bool
        Checks all the rows; returns true if there is a row
        where all elements are the same
        '''
        for i in range(0, len(self.the_board.the_board)):
            if (i % 3 == 2) and (self.the_board.the_board[i] == "X" or self.the_board.the_board[i] == "O") and (self.the_board.the_board[i] == self.the_board.the_board[i-1] and self.the_board.the_board[i] == self.the_board.the_board[i-2]):
                return True, self.the_board.the_board[i]
        return False, "-"

    def check_col(self):
        # Helper
        '''
        Sig: Game -> bool
        Checks all the columns; returns true if there is a column
        where all elements are the same
        '''
        for i in range(6, len(self.the_board.the_board)):
            if (self.the_board.the_board[i] == "X" or self.the_board.the_board[i] == "O") and (self.the_board.the_board[i] == self.the_board.the_board[i-3] and self.the_board.the_board[i] == self.the_board.the_board[i-6]):
                return True, self.the_board.the_board[i]
        return False, "-"

    def check_diag(self):
        # Helper
        '''
        Sig: Game -> bool
        Checks all the diagonals; returns true if there is a diagonal
        where all elements are the same
        '''
        for i in range(0, len(self.the_board.the_board)-5, 2):
            if (self.the_board.the_board[i] == "X" or self.the_board.the_board[i] == "O") and (self.the_board.the_board[i] == self.the_board.the_board[i+(4-i)] and self.the_board.the_board[i] == self.the_board.the_board[4+(4-i)]):
                return True, self.the_board.the_board[i]
        return False, "-"

    def check_full(self):
        # Helper
        '''
        Sig: Game -> bool
        Checks for an empty space; returns true if there is no
        empty space on the board
        '''
        if "_" not in self.the_board.the_board:
            return True
        return False

    def check_game_over(self):
        """
        signature: Game -> bool
        Given the current state of the board, determine
        if the game is over, by checking for
        a three-in-a-row pattern in horizontal,
        vertical, or diagonal lines; and also if the
        game has reached a stalemate, achieved when
        the board is full and no further move is possible.
        If there is a winner or if there is a stalemante, display
        an appropriate message to the user and clear the board
        in preparation for the next round. If the game is over,
        return True, otherwise False.
        """
        winner = self.check_row()[0] or self.check_col()[0] or self.check_diag()[0]
        no_winner = self.check_full()
        if winner or no_winner:
            return True
        return False

    def display_winner(self):
        # Helper
        '''
        Sig: Game -> bool
        Same function as check_game_over, however, this is used to print
        the results of the game
        '''
        check_winner = self.check_row()[0] or self.check_col()[0] or self.check_diag()[0]
        no_winner = self.check_full()
        winner = [self.check_row()[1], self.check_col()[1], self.check_diag()[1]]
        turtle.pencolor("cyan")
        if no_winner:
            turtle.goto(0, 0)
            turtle.write("NO WINNER!", align="center", font=("Arial", 100, "normal"))
            self.score_board.update_score("scoreboard.txt", "-", self.player_wins, self.computer_wins, self.round_num)
        elif "X" in winner:
            self.computer_wins += 1
            turtle.goto(0, 0)
            turtle.write("X WINS!", align="center", font=("Arial", 200, "normal"))
            self.score_board.update_score("scoreboard.txt", "X", self.player_wins, self.computer_wins, self.round_num)
        elif "O" in winner:
            self.player_wins += 1
            if self.score_board.get_highest_score("scoreboard.txt") < self.player_wins-self.computer_wins:
                turtle.pencolor("deep pink")
                turtle.goto(0, -150)
                turtle.write("HIGH SCORE", align="center", font=("Arial", 120, "bold"))
                turtle.pencolor("red")
                self.score_board.write("scoreboard.txt", "HIGH SCORE | ")
            turtle.goto(0, 0)
            turtle.pencolor("cyan")
            turtle.write("O WINS!", align="center", font=("Arial", 200, "normal"))
            self.score_board.update_score("scoreboard.txt", "O", self.player_wins, self.computer_wins, self.round_num)
            
        turtle.pencolor("red")
        self.round_num += 1
        self.reset()
                
    def do_computer_move(self):
        """
        signature: Game -> NoneType
        Given a list representing the state of the board,
        select a position for the computer's move and
        update the board with an X in an appropriate
        position. The algorithm for selecting the
        computer's move shall be as follows: if it is
        possible for the computer to win in one move,
        it must do so. If the human player is able 
        to win in the next move, the computer must
        try to block it. Otherwise, the computer's
        next move may be any random, valid position
        (selected with the random.randint function).
        """
        # Check if X can win in one move
        for i in range(0, len(self.the_board.the_board)):
            simulate_game = Game()
            simulate_game.the_board = copy.deepcopy(self.the_board)
            if self.the_board.the_board[i] == "_":
                simulate_game.the_board.the_board[i] = "X"
                if simulate_game.check_game_over() == True:
                    self.the_board.the_board[i] = "X"
                    return None
        # Check if X can block human move
        for i in range(0, len(self.the_board.the_board)):
            simulate_game = Game()
            simulate_game.the_board = copy.deepcopy(self.the_board)
            if self.the_board.the_board[i] == "_":
                simulate_game.the_board.the_board[i] = "O"
                if simulate_game.check_game_over() == True:
                    self.the_board.the_board[i] = "X"
                    return None
        # Get Corner or Center
        best_spots = [0, 2, 6, 8, 4]
        spots_ind = 0
        for i in range(0, len(self.the_board.the_board)):
            if self.the_board.the_board[i] == "_" and i in best_spots:
                self.the_board.the_board[i] = "X"
                return None
        # Random
        empty_spaces = []
        for i in range(0, len(self.the_board.the_board)):
            if self.the_board.the_board[i] == "_":
                empty_spaces.append(i)
        try: # Might get index = 0, empty_spaces[0] = IndexError
            index = random.randint(0, len(empty_spaces))
            self.the_board.the_board[empty_spaces[index]] = "X"
        except IndexError:
            pass
        
    def clickhandler(self, x, y):
        """
        signature: Game, int, int -> NoneType
        This function is called by turtle in response
        to a user click. The parameters are the screen
        coordinates indicating where the click happened.
        The function will call other functions. You do not
        need to modify this function, but you do need
        to understand it.
        """
        if self.do_user_move(x,y):
            self.the_board.draw_board()
            if not self.check_game_over():
                self.do_computer_move()
                self.the_board.draw_board()
        if self.check_game_over():
            self.display_winner()
            
    def play_game(self):
        """
        Signature: Game -> NoneType
        Runs the tic-tac-toe game.
        """
        self.later_init()
        
        turtle.onscreenclick(self.clickhandler)
        self.the_board.draw_board()
        
        turtle.mainloop()
        
def circle(radius):
    # Helper
    '''
    Sig: int -> NoneType
    Just draws a circle
    '''
    turtle.pensize(0)
    turtle.pendown()
    turtle.begin_fill()
    turtle.pencolor("black")
    turtle.circle(radius)
    turtle.color("yellow")
    turtle.end_fill()
    turtle.color("red")
    turtle.penup()
    turtle.pencolor("red")

def goTo(point):
    # Helper
    '''
    Sig: tuple(int, int) -> NoneType
    Difficult to keep track of each turtle orientation
    Easier to assume heading is always up
    '''
    (x, y) = point
    turtle.penup()
    turtle.goto(x,y)
    turtle.setheading(0)
    
def main():
    x = Game()
    x.play_game()
    
main()
