#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from IPython.display import clear_output
import random
from IPython.display import clear_output

def display_board(board):
    check=0
    for x in range(0,3):
        for y in range(0,3):
            print("|"+board[check],end='')
            check+=1
        print("|",end='')
        print("")  
   # print(board)
def player_input():
    
    player="xx"
    flag=True
    while flag:
        player=input("Please pick a marker for Player 1 'X' or 'O' : ").upper()
        if player=="X" or player=="O":
            flag=False
       # print(player)
        
        
    if player=="X":
        return "X","O"
    else:
        return "O","X"
    
    
def place_marker(board, marker, position):
    board[position-1]=marker
    

def win_check(board, mark):
    return (
        (board[0]==mark and board[1]==mark and board[2]==mark) or
        (board[3]==mark and board[4]==mark and board[5]==mark) or
        (board[6]==mark and board[7]==mark and board[8]==mark) or
        
        (board[0]==mark and board[3]==mark and board[6]==mark) or
        (board[1]==mark and board[4]==mark and board[7]==mark) or
        (board[2]==mark and board[5]==mark and board[8]==mark) or
        
        
        (board[0]==mark and board[4]==mark and board[8]==mark) or
        (board[2]==mark and board[4]==mark and board[6]==mark))



def choose_first():
    choose=random.randint(1,2)
    if choose==1:
        return "Player 1"
    else:
        return "Player 2"

    
    
def space_check(board, position):
    return board[position-1]==" "




def full_board_check(board):
 
    count=0
    for i in range(0,9):
        if(board[i]=="X" or board[i]=="O"):
            count+=1
    print(count)
    if count==9:
        return True
    else:
        return False
    



def player_choice(board,player):
    choicePosition=0
    while choicePosition not in [1,2,3,4,5,6,7,8,9] or not space_check(board,choicePosition):
        choicePosition=int(input(f"{player}: Please enter a number(1-9): "))

    return choicePosition


def replay():
    decision=input("Do you want to play again(yes / no): ").lower()
    if decision=="yes":
        return True
    else:
        return False

    
    
#==========================================================================================================================
playFlag=True
playAgain=True
while playAgain:
    
   # test_board = ['#','X','O','X','O','X','O','X','O','X']   
   # display_board(test_board) 
    print("====== WELCOME to Tic Tac Toe!!!! =======")
    player1_Marker,player2_Marker=player_input()

       
    li=list()
    li=[" "," "," "," "," "," "," "," "," "," "]


    turn=choose_first()
    
        
    print(f"{turn} GO FIRST")
    
    while playFlag:
        if turn=="Player 1":
            clear_output()
            display_board(li)
            position=player_choice(li,turn)
            place_marker(li,player1_Marker,position)
            if win_check(li,player1_Marker):
                clear_output()
                display_board(li)
                print(f"CONGRATULATION !!! Player 1 Won the game!!!")
                playFlag=False
            else:
                if full_board_check(li):
                    clear_output()
                    display_board(li)
                    print(f"Game Draw!!!")
                    playFlag=False
                    break
                else:
                    turn="Player 2"
        else:
            clear_output()
            display_board(li)
            position=player_choice(li,turn)
            place_marker(li,player2_Marker,position)
            
            if win_check(li,player2_Marker):
                clear_output()
                display_board(li)
                print(f"CONGRATULATION !!! Player 2 Won the game!!!")
                playFlag=False
            else:
                if full_board_check(li):
                    clear_output()
                    display_board(li)
                    print(f"Game Draw!!!")
                    playFlag=False
                    break
                else:
                    turn="Player 1"
    again=replay()
    if again==True:
        playFlag=True
        playAgain=True
    elif again==False:
        playFlag=False
        playAgain=False
        break
        
      



# In[ ]:





# In[ ]:





# In[ ]:




