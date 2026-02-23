def printTable():
    print(top)
    print(middle)
    print(bottom)

def playerMove(player):
    while True:
        row = int(input("Enter row: "))
        column  = int(input("Enter column: "))
        if row == 1:
            if top[column-1] == 0 and player == 1:
                top[column-1] = "X"
                break
            elif top[column-1] == 0 and player == 2:
                top[column-1] = "O"
                break
            else:
                print("Invalid choice, laready filled")
        elif row == 2:
            if middle[column-1] == 0 and player == 1:
                middle[column-1] = "X"
                break
            elif middle[column-1] == 0 and player == 2:
                middle[column-1] = "O"
                break
            else:
                print("Invalid choice, already filled")
        elif row == 3:
            if bottom[column-1] == 0 and player == 1:
                bottom[column-1] = "X"
                break
            elif bottom[column-1] == 0 and player == 2:
                bottom[column-1] = "O"
                break
            else:
                print("Invalid choice, already filled")
    printTable()
def gameLoop():
    ongoing = True
    while(ongoing):
        cTop = 0
        cMid = 0
        cBot = 0
        for i in top:
            if i == 0:
                cTop+=1
        for i in middle:
            if i == 0:
                cMid+=1
        for i in bottom:
            if i == 0:
                cBot+=1
        if cTop+cMid+cBot == 0:
            break
        else:
            playerMove(1)
            ongoing = checkWin()
            if ongoing == False:
                break
            playerMove(2)
            ongoing = checkWin()

def checkWin():
    if top[0] == top[1] == top[2] != 0:
        print(f"Player {'1' if top[0] == 'X' else '2'} wins!")
        return False
    if middle[0] == middle[1] == middle[2] != 0:
        print(f"Player {'1' if middle[0] == 'X' else '2'} wins!")
        return False
    if bottom[0] == bottom[1] == bottom[2] != 0:
        print(f"Player {'1' if bottom[0] == 'X' else '2'} wins!")
        return False
    if top[0] == middle[0] == bottom[0] != 0:
        print(f"Player {'1' if top[0] == 'X' else '2'} wins!")
        return False
    if top[1] == middle[1] == bottom[1] != 0:
        print(f"Player {'1' if top[1] == 'X' else '2'} wins!")
        return False
    if top[2] == middle[2] == bottom[2] != 0:
        print(f"Player {'1' if top[2] == 'X' else '2'} wins!")
        return False
    if top[0] == middle[1] == bottom[2] != 0:
        print(f"Player {'1' if top[0] == 'X' else '2'} wins!")
        return False
    if top[2] == middle[1] == bottom[0] != 0:
        print(f"Player {'1' if top[2] == 'X' else '2'} wins!")
        return False
    return True

top = [0,0,0]
middle = [0,0,0]
bottom = [0,0,0]
gameLoop()