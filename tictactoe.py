def tictactoe():
    board=[1,2,3,4,5,6,7,8,9]
    end=False
    wincombinations=((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(2,4,6),(0,4,8))
    def draw():
        print("   |   |   ")
        print(" "+str(board[0])+" |"+" "+str(board[1])+" |"+" "+str(board[2])+" ")
        print("---|---|---")
        print("   |   |   ")
        print(" "+str(board[3])+" |"+" "+str(board[4])+" |"+" "+str(board[5])+" ")
        print("---|---|---")
        print("   |   |   ")
        print(" "+str(board[6])+" |"+" "+str(board[7])+" |"+" "+str(board[8])+" ")
        print("---|---|---")
        print("   |   |   ")
    def p1():
            n=choosenumber()
            if board[n]=="X" or board[n]=="O":
                print("\nu can't go there,try again")
                p1()
            else:
                board[n]="X"
    def p2():
            n=choosenumber()
            if board[n]=="X" or board[n]=="O":
                print("\nu can't go there,try again")
                p2()
            else:
                board[n]="O"
    def choosenumber():
            while True:
                while True:
                    a=input()
                    try:
                        a=int(a)
                        a-=1
                        if a in range(0,9):
                            return a
                        else:
                            print("\nthat's not on the board,try again")
                            continue
                    except:
                        print("\nthat's not a number,try again")
                        continue
    def checkboard():
             count=0
             for a in wincombinations:
                 if board[a[0]]==board[a[1]]==board[a[2]]=="X":
                     print("player 1 wins!\n")
                     return True
                 if board[a[0]]==board[a[1]]==board[a[2]]=="O":
                     print("player 2 wins!\n")
                     return True
             for a in range(9):
                 if board[a]=="X" or  board[a]=="O"  :
                      count+=1
                 if count==9:
                      print("the game ends in a tie")
                      return True
    while not end:
            draw()
            end=checkboard()
            if end==True:
                break
            print("player 1 choose where to place a cross")
            p1()
            print()
            draw()
            end=checkboard()
            if end==True:
                break
            print("player 2 choose where to place a nought")
            p2()
            print()
    if input("play again(y/n)")=="y":
            print()
            tictactoe()
tictactoe()
                           
                           
                           
            
