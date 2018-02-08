import random
import time
import sys

class TicTacToe:
    def __init__(self, ai = (False, True)):
        print("Starting new TicTacToe game...")
        self.board = [['-' for i in range(3)] for i in range(3)]
        if ai[0]:
            self.player1name = 'Cortana'
        else:
            self.player1name = input("What is your name, player 1?")
        if ai[1]:
            self.player2name = "GLADOS"
        else:
            self.player2name = input("What is your name, player 2?")
        
        self.winstate = False
        self.moves = 0
        self.player = 0
        self.ai = ai 
        self.starting_UI()

    def play(self):
        self.make_move()
        self.print_board()
        self.moves += 1
        print(self.moves)
        
        if self.check_win():
            self.win_message()
            self.winstate = True 
        
        elif self.moves >= 9:
            self.draw_message()
            self.winstate = True
        else:
            self.player = (self.player + 1) % 2
            self.play()
    
    def make_move(self):
        player = self.player 
        if self.ai[player]:
            if player == 0:
                move = self.make_move_ai()
            else:
                move = self.make_move_ai()
        else:
            move = self.make_move_io()
        if player == 0:
            print(self.player1name + ' moves...')
            piece = 'X'
        else:
            print(self.player2name + ' moves...')
            piece = 'O'
        if self.ai[player]:
            time.sleep(1)
        self.board[move[0]][move[1]] = piece
      
    def make_move_ai(self):
        piece = self.set_piece()
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == '-':
                    self.board[i][j] = piece
                    if self.check_win():
                        self.board[i][j] = '-'
                        return (i, j)
                    self.board[i][j] = '-'
        
        player = (self.player + 1) % 2 
        piece = self.set_piece(player)
        
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == '-':
                    self.board[i][j] = piece
                    if self.check_win(player):
                        self.board[i][j] = '-'
                        return (i, j)
                    self.board[i][j] = '-'
        
        if self.board[1][1] == '-':
            return (1, 1)
        
        piece = self.set_piece()
        
        if self.board[1][1] == piece and self.moves == 3:
            if sum(self.board[pos[0]][pos[1]] !='-' for pos in [(0,0), (0,2), (2,0), (2,2)]) == 2:
                x = random.randint(0,3)
                return [(0,1), (1,0), (1,2), (2,1)][x]
            #if sum(self.board[pos[0]][pos[1]] !='-' for pos in [(1,2), (2,1)]) == 2:
            #    x = random.randint(0,2)
            #    return [(0,2), (2,0), (2,2)][x]
                
        for pos in [(0,0), (0,2), (2,0), (2,2), (0,1), (1,0), (1,2), (2,1)]:
            if self.board[pos[0]][pos[1]] == '-':
                return pos
        
    def make_move_ai2(self):
        attempt = random.randint(0, 8)
        move = (attempt // 3, attempt % 3)
        if self.board[move[0]][move[1]] != '-':
            move = self.make_move_ai()
        return move 
        
    def make_move_io(self):
        if self.player == 0:
            playername = self.player1name
        else:
            playername = self.player2name 
        move = input("What is your move, " + playername + '?')
        try:
            move = self.check_if_valid(move)
        except Exception as e:
            print(e)
            move = self.make_move_io()
        return move
    
    def check_if_valid(self, move):
        try:
            #row, column = (int(x) for x in move.split(" "))
            assert len(move) >= 2, "are you sure you have both a row and a column?"
            row, column = int(move[0]), int(move[-1])
        except:
            raise Exception("That is not a valid move!")
        if row < 0 or row >= 3 or column < 0 or column >= 3:
            raise Exception("move not on board!")
        elif self.board[row][column] != '-':
            raise Exception("cannot play in a position with another piece!")
        return (row, column)
    
    def check_win(self, player = None):
        piece = self.set_piece(player)
        for row in self.board:
            if sum(x == piece for x in row) == 3:
                return True
        
        for column in range(3):
            if sum(self.board[x][column] == piece for x in range(3)) == 3:
                return True 
        
        d1 = [(0,0), (1,1), (2,2)]
        d2 = [(0,2), (1,1), (2,0)]
        for diagonal in [d1, d2]:
            if sum(self.board[pos[0]][pos[1]] == piece for pos in diagonal) == 3:
                return True
        return False
    
    def set_piece(self, player = None):
        if player == None:
            player = self.player 
        if player == 0:
            piece = 'X'
        else:
            piece = 'O'
        return piece
            
    def starting_UI(self):
        print ("Here's how you enter moves on the board:")
        pboard = [[(i, j) for j in range(3)] for i in range(3)]
        #print(pboard)
        for row in pboard:
            r = [' '.join(str(x) for x in elem) for elem in row]
            print ('|'.join(r))
    def draw_message(self):
        print ("Game ends in a draw!")
        
    def win_message(self):
        if self.player == 0:
            print(self.player1name + " wins!")
        else:
            print(self.player2name + " wins!")
    
    def print_board(self):
        for row in self.board:
            print('|'.join(row))

# End of TicTacToe class.

def launch_game(num):
    num = int(num) % 4
    mapping = {0: (True, True), 1: (False, True), 2: (True, False), 3: (False, False)}
    game = TicTacToe(mapping[num])
    game.play()

def keep_playing(playing):
    if len(playing) == 0:
        return False 
    if playing[0].lower() in ['f','n', 'e','q']:
        return False
    return True
def system_communication():
    if sys.argv[1] in ['1','2','3','4']:
        launch_game(int(sys.argv[1]))
    else:
        mode = 'ok'
        while mode != '':
            print ("There are 4 modes of the Tic Tac Toe game:")
            print ("1: Go first against the AI")
            print ("2: Play second against the AI")
            print ("3: Play against a friend")
            print ("4: pit two AIs against each other!")
            mode = input("Which game mode are you most interested in?")
            try:
                m = int(mode)
                launch_game(m)
                playing = input("Do you want to keep playing?")
            except:
                playing = input("I didn't catch that. Do you want to keep playing?")
            if not keep_playing(playing):
                break
                
        print("Have a nice day!")

if len(sys.argv) == 1:
    game = TicTacToe((False, True)) 
    game.play()
else:
    system_communication()