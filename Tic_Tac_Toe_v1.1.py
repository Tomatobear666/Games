 # The idea is to add 1 to a row or line or dialonal if player A places a move on it. If player B: -1. If one row or line or diagonal has 3 or -3, A / B has won the game.
 # So at the start all rows, lines and diagonals are 0
fline = sline = tline = frow = srow = trow = rupdia = lupdia = 0
Awin = Bwin =False


def addpointA(num):  # add the point to the var of the row/line/diagonal after A has made a move
    global fline, sline, tline, frow, srow, trow, rupdia, lupdia
    if num < 4:
        fline = fline + 1
    if 3 < num < 7:
        sline = sline+ 1
    if num > 6:
        tline = tline + 1
    if num % 3 == 1:
        frow = frow + 1
    if num % 3 == 2:
        srow = srow + 1
    if num % 3 == 0:
        trow = trow + 1
    if num % 4 == 1:
        rupdia = rupdia + 1
    if num % 2 == 1 and 2 < num < 8:
        lupdia = lupdia + 1

def addpointB(num):  # Same thing with B, so -1
    global fline, sline, tline, frow, srow, trow, rupdia, lupdia
    if num < 4:
        fline = fline - 1
    elif num < 7:
        sline = sline- 1
    else:
        tline = tline - 1
    if num % 3 == 1:
        frow = frow - 1
    if num % 3 == 2:
        srow = srow - 1
    if num % 3 == 0:
        trow = trow - 1
    if num % 4 == 1:
        rupdia = rupdia - 1
    if num % 2 == 1 and 2 < num < 8:
        lupdia = lupdia - 1


def checkwin():  #Check if anybody has won the game
    global fline, sline, tline, frow, srow, trow, rupdia, lupdia, Awin, Bwin
    if fline == 3 or sline == 3 or tline == 3 or frow == 3 or srow == 3  or trow == 3 or rupdia == 3 or lupdia == 3 :
        Awin = True
    if fline == -3 or sline == -3 or tline == -3 or frow == -3 or srow == -3  or trow == -3 or rupdia == -3 or lupdia == -3 :
        Bwin = True

#Now I add the funktions to simplyfy the code
def moveA(num, playr):
    inputmove = int(input(playr+", make the "+num+" move: "))
    addpointA(inputmove)

def moveB(num, playr):
    inputmove = int(input(playr+", make the "+num+" move: "))
    addpointB(inputmove)

def cwinA():
    checkwin()
    if Awin == True:
        print(Aname+" has won the game!")
        quit()

def cwinB():
    checkwin()
    if Bwin == True:
        print(Bname+" has won the game!")
        quit()


Aname = input("Player A, please enter your name: ")
Bname = input("Player B, please enter your name: ")
print("Hello",Aname,"and",Bname)

# Now it's the real programm: it takes the move and adds the point

moveA("1.", Aname)
moveB("2.", Bname)
moveA("3.", Aname)
moveB("4.", Bname)
#Now, it is possible that somebody could win, so checkwin
moveA("5.", Aname)
cwinA()
moveB("6.", Bname)
cwinB()
moveA("7.", Aname)
cwinA()
moveB("8.", Bname)
cwinB()
moveA("9.", Aname)
cwinA()
print("The game ended in a draw") # If the programm hasn't quit jet, is means that nobody has won.
'''
#print(fline,sline,tline,frow,srow,trow,leftupdia,rightupdia)
'''

