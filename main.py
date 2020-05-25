num = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]



class Win():
    game = True
    line = ""
    a = 0
    def checkIfWin(self):
        # check row 0
        if num[0][0] == num[0][1] and num[0][1] == num[0][2]:
            if num[0][0] != "-":
                self.line = num[0][0]

        # check row 1
        elif num[1][0] == num[1][1] and num[1][1] == num[1][2]:
            if num[1][0] != "-":
                self.line = num[1][0]

        # check row 2
        elif num[2][0] == num[2][1] and num[2][1] == num[2][2]:
            if num[2][0] != "-":
                self.line = num[2][0]

        # check collum 0
        elif num[0][0] == num[1][0] and num[1][0] == num[2][0]:
            if num[0][0] != "-":
                self.line = num[0][0]

        # check collum 1
        elif num[0][1] == num[1][1] and num[1][1] == num[2][1]:
            if num[0][1] != "-":
                self.line = num[0][1]

        # check collum 2
        elif num[0][2] == num[1][2] and num[1][2] == num[2][2]:
            if num[0][2] != "-":
                self.line = num[0][2]

        # angle bottom
        elif num[0][0] == num[1][1] and num[1][1] == num[2][2]:
            if num[0][0] != "-":
                self.line = num[0][0]

        # angle top
        elif num[2][0] == num[1][1] and num[1][1] == num[0][2]:
            if num[2][0] != "-":
                self.line = num[2][0]

        if self.line == "X":
            print("Player 1 Won")
            self.game = False
        elif self.line == "O":
            print("Player 2 Won")
            self.game = False
        else:
            self.a += 1
            if self.a == 9:
                print("Is a Draw")
                self.game = False


players = Win()


def player1():
    while players.game:

        try:
            i = int(input("Player 1: "))
        except:
            print("Enter a number")
            player1()
        try:
            if i <= 3:
                if num[0][i - 1] != "-":
                    print("Please try another number")
                    player1()
                else:
                    num[0][i - 1] = "X"
                    print("+-----------+")
                    print("| " + num[0][0] + ' | ' + num[0][1] + " | " + num[0][2] + " |")
                    print("| " + num[1][0] + ' | ' + num[1][1] + " | " + num[1][2] + " |")
                    print("| " + num[2][0] + ' | ' + num[2][1] + " | " + num[2][2] + " |")
                    print("+-----------+")
                    players.checkIfWin()
                    player2()
            elif i <= 6:
                if num[1][i - 4] != "-":
                    print("Please try another number")
                    player1()
                else:
                    num[1][i - 4] = "X"
                    print("+-----------+")
                    print("| " + num[0][0] + ' | ' + num[0][1] + " | " + num[0][2] + " |")
                    print("| " + num[1][0] + ' | ' + num[1][1] + " | " + num[1][2] + " |")
                    print("| " + num[2][0] + ' | ' + num[2][1] + " | " + num[2][2] + " |")
                    print("+-----------+")
                    players.checkIfWin()
                    player2()
            elif i <= 9:
                if num[2][i - 7] != "-":
                    print("Please try another number")
                    player1()
                else:
                    num[2][i - 7] = "X"
                    print("+-----------+")
                    print("| " + num[0][0] + ' | ' + num[0][1] + " | " + num[0][2] + " |")
                    print("| " + num[1][0] + ' | ' + num[1][1] + " | " + num[1][2] + " |")
                    print("| " + num[2][0] + ' | ' + num[2][1] + " | " + num[2][2] + " |")
                    print("+-----------+")
                    players.checkIfWin()
                    player2()
        except:
            break


def player2():
    while players.game:
        try:
            i = int(input("Player 2: "))
        except:
            print("Enter a number")
            player2()

        if i <= 3:
            if num[0][i - 1] != "-":
                print("Please try another number")
                player2()
            else:
                num[0][i - 1] = "O"
                print("+-----------+")
                print("| " + num[0][0] + ' | ' + num[0][1] + " | " + num[0][2] + " |")
                print("| " + num[1][0] + ' | ' + num[1][1] + " | " + num[1][2] + " |")
                print("| " + num[2][0] + ' | ' + num[2][1] + " | " + num[2][2] + " |")
                print("+-----------+")
                players.checkIfWin()
                player1()
        elif i <= 6:
            if num[1][i - 4] != "-":
                print("Please try another number")
                player2()
            else:
                num[1][i - 4] = "O"
                print("+-----------+")
                print("| " + num[0][0] + ' | ' + num[0][1] + " | " + num[0][2] + " |")
                print("| " + num[1][0] + ' | ' + num[1][1] + " | " + num[1][2] + " |")
                print("| " + num[2][0] + ' | ' + num[2][1] + " | " + num[2][2] + " |")
                print("+-----------+")
                players.checkIfWin()
                player1()

        elif i <= 9:
            if num[2][i - 7] != "-":
                print("Please try another number")
                player2()
            else:
                num[2][i - 7] = "O"
                print("+-----------+")
                print("| " + num[0][0] + ' | ' + num[0][1] + " | " + num[0][2] + " |")
                print("| " + num[1][0] + ' | ' + num[1][1] + " | " + num[1][2] + " |")
                print("| " + num[2][0] + ' | ' + num[2][1] + " | " + num[2][2] + " |")
                print("+-----------+")
                players.checkIfWin()
                player1()



print("+-----------+")
print("| " + num[0][0] + ' | ' + num[0][1] + " | " + num[0][2] + " |")
print("| " + num[1][0] + ' | ' + num[1][1] + " | " + num[1][2] + " |")
print("| " + num[2][0] + ' | ' + num[2][1] + " | " + num[2][2] + " |")
print("+-----------+")
player1()