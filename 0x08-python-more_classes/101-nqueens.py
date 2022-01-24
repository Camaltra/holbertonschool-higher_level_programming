import sys

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if not sys.argv[1].isdigit:
        print("N must be a number")
        exit(1)
    numOfQueen = int(sys.argv[1])
    if numOfQueen < 4:
        print("N must be at least 4")
        exit(1)

    res = []
    for i in range(numOfQueen):
        res.append([i, None])

    def clearRes(x):
        for i in range(x, numOfQueen):
            res[i][1] = None

    def possible(x, y):
        for z in range(numOfQueen):
            if y == res[z][1]:
                return False
        i = 0
        while(i < x):
            if abs(res[i][1] - y) == abs(i - x):
                return False
            i += 1
        return True

    def nqueens(x):
        for y in range(numOfQueen):
            clearRes(x)
            if possible(x, y):
                res[x][1] = y
                if (x == numOfQueen - 1):
                    print(res)
                else:
                    nqueens(x + 1)

    nqueens(0)
