fline = 0 # The idea is to add 1 to a row or line or dialonal if player A places a move on it. If player B: -1. If one row or line or diagonal has 3 or -3, A / B has won the game.
sline = 0 # So at the start all rows, lines and diagonals are 0
tline = 0
frow = 0
srow = 0
trow = 0
leftupdia = 0
rightupdia = 0
Awin = False
Bwin = False


def addpointA(num):  # add the point to the var of the row/line/diagonal after A has made a move
    global fline
    global sline
    global tline
    global frow
    global srow
    global trow
    global leftupdia
    global rightupdia
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
        leftupdia = leftupdia + 1
    if num % 2 == 1 and 2 < num < 8:
        rightupdia = rightupdia + 1

def addpointB(num):  # Same thing with B, so -1
    global fline
    global sline
    global tline
    global frow
    global srow
    global trow
    global leftupdia
    global rightupdia
    if num < 4:
        fline = fline - 1
    if 3 < num < 7:
        sline = sline- 1
    if num > 6:
        tline = tline - 1
    if num % 3 == 1:
        frow = frow - 1
    if num % 3 == 2:
        srow = srow - 1
    if num % 3 == 0:
        trow = trow - 1
    if num % 4 == 1:
        leftupdia = leftupdia - 1
    if num % 2 == 1 and 2 < num < 8:
        rightupdia = rightupdia - 1


def checkwin():  #Check if anybody has won the game
    global fline
    global sline
    global tline
    global frow
    global srow
    global trow
    global leftupdia
    global rightupdia
    global Awin
    global Bwin
    if fline == 3 or sline == 3 or tline == 3 or frow == 3 or srow == 3  or trow == 3 or leftupdia == 3 or rightupdia == 3 :
        Awin = True
    if fline == -3 or sline == -3 or tline == -3 or frow == -3 or srow == -3  or trow == -3 or leftupdia == -3 or rightupdia == -3 :
        Bwin = True

# Now it's the real programm: it takes the move and adds the point
fmove = int(input("Player A: make your first move:"))
addpointA(fmove)

smove = int(input("Player B: make the seconde move:"))
addpointB(smove)

tmove = int(input("Player A: make the third move:"))
addpointA(tmove)

fourmove = int(input("Player B: make the fourth move:"))
addpointB(fourmove)

#Now, it is possible that somebody could win, so checkwin
fivemove = int(input("Player A: make the fifth move:"))
addpointA(fivemove)
checkwin()
if Awin == True:
    print("A has won the game!")
    quit()


sixmove = int(input("Player B: make the sixth move:"))
addpointB(sixmove)
checkwin()
if Bwin == True:
    print("B has won the game!")
    quit()


sevenmove = int(input("Player A: make the seventh move:"))
addpointA(sevenmove)
checkwin()
if Awin == True:
    print("A has won the game!")
    quit()

eightmove = int(input("Player B: make the eighth move:"))
addpointB(eightmove)
checkwin()
if Bwin == True:
    print("B has won the game!")
    quit()

ninemove = int(input("Player A: make the nineth move:"))
addpointA(ninemove)
checkwin()
if Awin == True:
    print("A has won the game!")
    quit()
else:
    print("The game ended in a draw.")



'''
#print(fline,sline,tline,frow,srow,trow,leftupdia,rightupdia)
'''

