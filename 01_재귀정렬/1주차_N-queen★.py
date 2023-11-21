n = int(input())
# pos = [0]*n #각 열에 배치한 퀸의 위치
# queens move diagonally, vertically and horizontally
# therefore they can't be on the same rows or columns
# hash set ->  no duplicates
def solveQueens(n: int):
    col = set()
    posDiag = set() # r+c (left bottom to right top)
    negDiag = set() # r-c (left bottom to right top)

    res =[]
    # board = [["."]*n for i in range(n)]
    def backtrack(r):
        if r==n:
            # copy = ["".join(row)for row in board]
            res.append(1)
            return
        
        for c in range(n):
            if c in col or (r+c) in posDiag or (r-c) in negDiag: #queen is already in the column or row or diagonal postion
                    continue 
            
            # add queen on board
            col.add(c)
            posDiag.add(r+c)
            negDiag.add(r-c)
            # board[r][c]="Q"
            
            backtrack(r+1)
            
            col.remove(c)
            posDiag.remove(r+c)
            negDiag.remove(r-c)
            # board[r][c]="."
                  
    backtrack(0)
    return len(res)
        
print(solveQueens(n))