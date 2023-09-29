#Tic Tac Toe Using Min-Max Algorithm
def print_bd(bd):
    for row in bd:
        print("    |  ".join(row))

        print("-----" * 4)

def check_winner(bd, player):
    for i in range(3):
        if bd[i][0] == bd[i][1] == bd[i][2] == player:
            return True
        if bd[0][i] == bd[1][i] == bd[2][i] == player:
            return True

    if bd[0][0] == bd[1][1] == bd[2][2] == player:
        return True
    if bd[0][2] == bd[1][1] == bd[2][0] == player:
        return True

    return False

def minimax(bd, depth, is_maximizing):
    if check_winner(bd, ' X'):
        return -10
    if check_winner(bd, 'O'):
        return 10
    if all(cell != ' ' for row in bd for cell in row):
        return 0

    if is_maximizing:
        best = -float('inf')
        for i in range(3):
            for j in range(3):
                if bd[i][j] == ' ':
                    bd[i][j] = 'O'
                    best = max(best, minimax(bd, depth + 1, not is_maximizing) - depth)
                    bd[i][j] = ' '
        return best
    else:
        best = float('inf')
        for i in range(3):
            for j in range(3):
                if bd[i][j] == ' ':
                    bd[i][j] = ' X'
                    best = min(best, minimax(bd, depth + 1, not is_maximizing) + depth)
                    bd[i][j] = ' '
        return best

def ai_move(bd):
    best_score = -float('inf')
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if bd[i][j] == ' ':
                bd[i][j] = 'O'
                score = minimax(bd, 0, False)
                bd[i][j] = ' '
                if score > best_score:
                    best_score = score
                    best_move = (i, j)

    return best_move

def main():
    bd = [[" " for _ in range(3)] for _ in range(3)]
    turns = 0

    while turns < 9:
        print_bd(bd)

        if turns % 2 == 0:
            print("Your turn (X)")

            while True:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter column (0-2): "))

                if 0 <= row <= 2 and 0 <= col <= 2 and bd[row][col] == " ":
                    break
                else:
                    print("Invalid move. Try again!")

            bd[row][col] = ' X'
        else:
            print("AI's turn (O)")
            row, col = ai_move(bd)
            bd[row][col] = 'O'

        if check_winner(bd, 'X'):
            print_bd(bd)
            print("You win!")
            return
        elif check_winner(bd, 'O'):
            print_bd(bd)
            print("AI wins!")
            return

        turns += 1

    print_bd(bd)
    print("Match draw!")

if __name__== "__main__":
    main()