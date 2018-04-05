

def printBoard(xList, oList) :

### THIS FUNCTION JUST PRINTS OUT THE CURRENT STATUS OF THE TIC TAC TOE BOARD
## input : cells reserved by player X, cells reserved by player O
## output : Status of the board

    myNewList = []
    for i in range(1, 10) :
        if i in xList :
            myNewList.append('X')
        elif i in oList :
            myNewList.append('O')
        else :
            myNewList.append(' ')

    print('\n\n')
    print(' {} | {} | {} '.format(myNewList[0], myNewList[1], myNewList[2]))
    print('___|___|___')
    print(' {} | {} | {} '.format(myNewList[3], myNewList[4], myNewList[5]))
    print('___|___|___')
    print(' {} | {} | {} '.format(myNewList[6], myNewList[7], myNewList[8]))
    print('   |   |   ')
    print('\n\n')

def winningCombinations() :

    ## This function just knows the winning combinations
    ## input : None
    ## output : None

        winningCombinations = {}
        winningCombinations[1] = [[1,2,3], [1, 5, 9], [1, 4, 7]]
        winningCombinations[2] = [[1, 2, 3], [2, 5, 8]]
        winningCombinations[3] = [[1, 2, 3], [3, 5, 7], [3, 6, 9]]
        winningCombinations[4] = [[1, 4, 7], [4, 5, 6]]
        winningCombinations[5] = [[1, 5, 9], [2, 5, 8], [3, 5, 7]]
        winningCombinations[6] = [[4, 5, 6], [3, 6, 9]]
        winningCombinations[7] = [[1, 4, 7], [3, 5, 7], [7, 8, 9]]
        winningCombinations[8] = [[2, 5, 8], [7, 8, 9]]
        winningCombinations[9] = [[1, 5, 9], [7, 8, 9], [3, 6, 9]]

        return winningCombinations


def checkWinner(xList, oList, move, player1, player2, turn) :

    ## This function checks if there is any winner after the last move.
    ## input : Cells reserved by players, player who made the last turn, cell last reserved(move)
    ## output : True if a player wins or false if none wins

    wc = winningCombinations()
    lis = wc[move]
    count = 0
    if turn :
        if player1.lower() == 'x' :
            for winEntry in lis :
                for eachEntry in winEntry :
                    if eachEntry in xList :
                        count += 1
                    else :
                        count = 0
                        break
                    if count == 3 :
                        return True, player1

        elif player1.lower() == 'o' :
            for winEntry in lis :
                for eachEntry in winEntry :
                    if eachEntry in oList :
                        count += 1
                    else :
                        count = 0
                        break
                    if count == 3 :
                        return True, player1

    else :

        if player2.lower() == 'x' :
            for winEntry in lis :
                for eachEntry in winEntry :
                    if eachEntry in xList :
                        count += 1
                    else :
                        count = 0
                        break
                    if count == 3 :
                        return True, player2

        elif player2.lower() == 'o' :
            for winEntry in lis :
                for eachEntry in winEntry :
                    if eachEntry in oList :
                        count += 1
                    else :
                        count = 0
                        break
                    if count == 3 :
                        return True, player2

    printBoard(xList, oList)
    return False, ''

def beginGame() :

    ## This function initialises the game.
    ## input : None
    ## output : None

    print('\n\n')
    print("\t\t\t\t\tWELCOME TO THE GAME.\n\n\t\t\t\t\tIT'S TIC TAC TOE.\n")
    print('\t\t\t\t\tPlease note the numbers for the cell as shown below.\n')
    print('\t\t\t\t\t\t\t 1 | 2 | 3 ')
    print('\t\t\t\t\t\t\t___|___|___')
    print('\t\t\t\t\t\t\t 4 | 5 | 6')
    print('\t\t\t\t\t\t\t___|___|___')
    print('\t\t\t\t\t\t\t 7 | 8 | 9')
    print('\t\t\t\t\t\t\t   |   |   ')
    print('\n\n')


    while True :

        player1 = input('X or O ? : ')
        player2 = ''
        if player1.lower() == 'x' :
            player2 = 'o'
            break

        elif player1.lower() == 'o':
            player2 = 'x'
            break

        else :
            continue

    xList = []
    oList = []
    turn = True
    noOfMoves = 0

    printBoard(xList, oList)

    return xList, oList, turn, player1, player2, noOfMoves

def makeMove(xList, oList, player1, player2, turn, noOfMoves) :

    ## This function reserves the cell as asked by the player whose turn it is.
    ## input : Already reserved cells, whose turn it is, total number of moves made till now.
    ## output : None

    while True :
        if turn :
            print("{}'s turn".format(player1.upper()))
        else :
            print("{}'s turn".format(player2.upper()))
        while True :
            try :
                move = int(input('which cell should be marked (1 - 9) ? :'))
                break
            except :
                continue

        if move > 0 and move < 10 and move not in oList and move not in xList :
            break
        else :
            print('\nINVALID MOVE\n')
            printBoard(xList, oList)

    if turn :

        if player1.lower() == 'x' :
            xList.append(move)
            #print(f'appending move {move} to xList for player1')
        else :
            oList.append(move)
            #print(f'appending move {move} to oList for player1')

    else :

        if player2.lower() == 'x' :
            xList.append(move)
            #print(f'appending move {move} to xList for player2')
        else :
            oList.append(move)
            #print(f'appending move {move} to oList for player2')

    noOfMoves += 1

    return xList, oList, move, turn, noOfMoves


if __name__ == '__main__' :

    xList, oList, turn, player1, player2, noOfMoves = beginGame()

    while True :
        xList, oList, move, turn, noOfMoves = makeMove(xList, oList, player1, player2, turn, noOfMoves)
        isWinner, winner = checkWinner(xList, oList, move, player1, player2, turn)
        turn = not turn

        if isWinner :
            print('player who chose {} wins.'.format(winner.upper()))
            printBoard(xList, oList)
            option = input('New Game ? (Y/ N): ')
            if option.lower() == 'y' :
                xList, oList, turn, player1, player2, noOfMoves = beginGame()
                continue
            else :
                break
        elif noOfMoves == 9 :
            print("It's a draw")
            option = input('New Game ? (Y/ N): ')
            if option.lower() == 'y' :
                xList, oList, turn, player1, player2, noOfMoves = beginGame()
                continue
            else :
                break
        else :
            continue
