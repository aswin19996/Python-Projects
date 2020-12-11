from random import randrange
def DisplayBoard(board):
#
# the function accepts one parameter containing the board's current status
# and prints it out to the console
#

#to print the Board
    r=4
    c=4
    row=0;
    column=0;
    flag=0
    for i in range (25):
       if(int(i%2)==0): 
        if (int(i%8)==0):
            for j in range(25):
                if((int(j%8))==0): print("+", end="");
                else:print("-",end="");
        else:
            c=4;
            column=0;
            for j in range(25):
                if(i==r and j==c):
                        c=j+8
                        print(board[row][column], end="")
                        column=column+1
                        flag=flag+1
                elif((int(j%8))==0):print("|", end="");
                else:print(" ",end="");
                if (flag!=0 and flag%3==0):
                    r=i+8;
                    row=row+1
                    flag=0;
        print();
        #MakeListOfFreeFields(board);
        
    return

def EnterMove(board):
#
# the function accepts the board current status, asks the user about their move, 
# checks the input and updates the board according to the user's decision
#
 global countO
 countO=countO+1;
 while(1):
    
    i=int(input("Enter Your Move:"));
    if i in pos_to_num_map.keys():
        
        if i in range(1,4):
            board[0][i-1]='O';
            break
        elif i in range(4,7):
            board[1][i-4]='O';
            break
        elif i in range(7,10):
            board[2][i-7]='O';
            break
        else:
            print("Enter Again:...")
            continue
    else:
        print("Enter Again:...")
        continue
 
   
 if countO>2: VictoryFor(board,'O');
 return

def MakeListOfFreeFields(board):
#
# the function browses the board and builds a list of all the free squares; 
# the list consists of tuples, while each tuple is a pair of row and column numbers
#
    #boardcheck()
    global pos_to_num_map
    pos_to_num_map={}
    boardpos=0
    freespace=[];
    equals_flag=0;
    for row in range(3):
        for column in range(3):
            boardpos=boardpos+1
            if board[row][column]!= 'X' and board[row][column]!= 'O':
                freespace.append((row,column));
                d=freespace[-1]
                pos_to_num_map[boardpos]=d;
                
   #to print freespace.....!
                
   # for i in freespace:print(i)
    #print(pos_to_num_map)
    b=bool(pos_to_num_map)
    if not b:
        #print("Entered Draw Condition")       
        global draw
        draw=1
        VictoryFor(board,'X')
    
    return    
def VictoryFor(board, sign):
#
# the function analyzes the board status in order to check if 
# the player using 'O's or 'X's has won the game
#
    #print("entererd VictoryFor")
    #print(pos_to_num_map)
    #print(draw)
    
    if draw==1:
            print("Match Drawed")
            exit()
    if (board[0][0]==sign):
        if(board[0][1]==sign and board[0][2]==sign):
            if sign=='X':
                DisplayBoard(board);
                print("Computer Wins")
                #print("by row 1")
                exit()
            else:
                DisplayBoard(board);
                print("You Win")
                #print("by row 1")
                exit()
    
        elif (board[1][0]==sign and board[2][0]==sign):
            if sign=='X':
                DisplayBoard(board);
                print("Computer Wins")
                #print("by col 1")
                exit()
            else:
                DisplayBoard(board);
                print("You Win")
                #print("by col 1")
                exit()
    elif (board[1][1]==sign):
        if(board[0][1]==sign and board[2][1]==sign):
            if sign=='X':
                DisplayBoard(board);
                print("Computer Wins")
                #print("by col 2")
                exit()
            else:
                DisplayBoard(board);
                print("You Win")
                #print("by col 2")
                exit()
        elif (board[1][0]==sign and board[1][2]==sign):
            if sign=='X':
                DisplayBoard(board);
                print("Computer Wins")
                #print("by row 2")
                exit()
            else:
                DisplayBoard(board);
                print("You Win")
                #print("by row 2")
                exit()
        elif (board[2][0]==sign and board[0][2]==sign):
                DisplayBoard(board);
                print("Computer Wins");
                #print("by Right Diagonally")
                exit()
        elif (board[0][0]==sign and board[2][2]==sign):
                DisplayBoard(board);
                
                print("Computer Wins")
                #print("by Left diagonally")
                exit()
    elif (board[2][2]==sign):
        if(board[0][2]==sign and board[1][2]==sign):
            if sign=='X':
                DisplayBoard(board);
                print("Computer Wins")
                #print("by col 3")
                exit()
            else:
                DisplayBoard(board);
                print("You Win")
                #print("by col 3")
                exit()
        elif (board[2][0]==sign and board[2][1]==sign):
            if sign=='X':
                DisplayBoard(board);
                print("Computer Wins")
                #print("by row 3")
                exit()
            else:
                DisplayBoard(board);
                print("You Win")
                #print("by row 3")
                exit()
    
    
            
    return
def DrawMove(board):
#
# the function draws the computer's move and updates the board
#
    global countX;
    if countX==0:
        board[1][1]='X'
        countX=countX+1;
    else:
     while(1):
        num=randrange(1,10);
        if num in pos_to_num_map.keys():
            row=pos_to_num_map[num][0];
            column=pos_to_num_map[num][1];
            board[row][column]='X';
            countX=countX+1;
            if countX>2:
                VictoryFor(board,'X')
                
            break;
        else:continue;
    return
def boardcheck():
    print(board)
    for row in range(3):
        for column in range(3):
            print(board[row][column])
    return

board=[];

draw=0

for i in range(3):
    board.append([]);
k=0;
for i in range(0,3):
   board[i].append(k+1);
   board[i].append(k+2); 
   board[i].append(k+3);
   k=k+3

tictactoe=1;
countX=0;
countO=0;
pos_to_num_map={}

DrawMove(board);
MakeListOfFreeFields(board);
DisplayBoard(board);

while(1):
    
    if tictactoe==0:
        DrawMove(board);
        tictactoe=1;
    else:
        EnterMove(board);
        tictactoe=0;
    DisplayBoard(board);
    MakeListOfFreeFields(board);
    





