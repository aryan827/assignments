b = [' ' for x in range(10)]

def insertLetter(letter, place):
    b[place] = letter

def spaceIsFree(place):
    return b[place] == ' '

def printBoard(b):
    print('   |   |')
    print(' ' + b[1] + ' | ' + b[2] + ' | ' + b[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + b[4] + ' | ' + b[5] + ' | ' + b[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + b[7] + ' | ' + b[8] + ' | ' + b[9])
    print('   |   |')
    
def isWinner(bo, l):
    return (bo[7] == l and bo[8] == l and bo[9] == l) or (bo[4] == l and bo[5] == l and bo[6] == l) or(bo[1] == l and bo[2] == l and bo[3] == l) or(bo[1] == l and bo[4] == l and bo[7] == l) or(bo[2] == l and bo[5] == l and bo[8] == l) or(bo[3] == l and bo[6] == l and bo[9] == l) or(bo[1] == l and bo[5] == l and bo[9] == l) or(bo[3] == l and bo[5] == l and bo[7] == l)

def playerMove():
    run = True
    while run:
        move = input('Please input position btw 1 to 9 ')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('X', move)
                else:
                    print('enter another place')
            else:
                print('enter within range')
        except:
            print('wrong input')
            

def compMove():
    pm = [t for t, letter in enumerate(b) if letter == ' ' and t != 0]
    move = 0

    for j in ['O', 'X']:
        for i in pm:
            boardCopy = b[:]
            boardCopy[i] = j
            if isWinner(boardCopy, j):
                move = i
                return move

    corner = []
    for i in pm:
        if i in [1,3,7,9]:
            corner.append(i)
            
    if len(corner) > 0:
        move = selectRandom(corner)
        return move

    if 5 in pm:
        move = 5
        return move

    edges = []
    for i in pm:
        if i in [2,4,6,8]:
            edges.append(i)
            
    if len(edges) > 0:
        move = selectRandom(edges)
        
    return move

def selectRandom(li):
    import random
    l = len(li)
    r = random.randrange(0,l)
    return li[r]
    

def isBoardFull(b):
    if b.count(' ') > 1:
        return False
    else:
        return True

def main():
    print('Lets start game')
    printBoard(b)

    while not(isBoardFull(b)):
        if not(isWinner(b, 'O')):
            playerMove()
            printBoard(b)
        else:
            print('0\'s won')
            break

        if not(isWinner(b, 'X')):
            move = compMove()
            if move == 0:
                print('game tie')
            else:
                insertLetter('O', move)
                print('O\' in position', move , ':')
                printBoard(b)
        else:
            print('X\'s won ')
            break

    if isBoardFull(b):
        print('game tie')

while True:
    answer = input(' want to play! (Y/N)')
    if answer.lower() == 'y' or answer.lower == 'yes':
        b = [' ' for x in range(10)]
        print('--------------------------------')
        main()
    else:
        break