import numpy as np 

board = [[3*i+j+1 for j in range(3)]for i in range(3)]

def c(board):
    ret = 0
    for i in board:
        for j in i:
            if type(j) is int:
                ret += 1
    return ret

def pr(board):
    for i in board:
        for j in i:
            print(str(j)+" ",end="")
        print("")

def rotate(board):
    return list(list(x)[::-1] for x in zip(*board))

def mate(board):
    if ["o","o","o"] in board:
        return "o"
    elif ["x","x","x"] in board:
        return "x"
    rot = rotate(board)
    if ["o","o","o"] in rot:
        return "o"
    elif ["x","x","x"] in rot:
        return "x"
    pos1 = 0
    pos2 = 2
    sc1 = 0
    sc2 = 0
    t1 = 0
    t2 = 0
    for r in np.arange(3):
        p1 = board[r][pos1]
        p2 = board[r][pos2]
        pos1 += 1
        pos2 -= 1
        if type(p1) is int:
            sc1 = 1
        elif p1 == "o":
            t1 += 1
        else:
            t1 -= 1
        if type(p2) is int:
            sc2 = 1
        elif p2 == "o":
            t2 += 1
        else:
            t2 -= 1
        if sc1 and sc2:
            break
    if t1 == 3 or t2 == 3:
        return "o"
    elif t1 == -3 or t2 == -3:
        return "x"
    tie = 0
    for i in board:
        for j in i:
            if type(j) is int:
                break
            else:
                tie += 1
    if tie == 9:
        return None    
    return False
        
def minimax(board,pl,depth,max_ = True):
    if depth == 0:
        m = mate(board)
        if m is False or m is None:
            return 0
        elif m is pl:
            return 1
        else:
            return -1
    else:
        scores = []
        pos = []
        for i in np.arange(3):
            for j in np.arange(3):
                if type(board[i][j]) is int:
                    nb = board[:]
                    nb[i][j] = pl
                    m = mate(nb)
                    if m is False or m is None:
                        m = minimax(nb,pl,depth-1,not max_)
                    elif m is pl:
                        m = 1
                    else:
                        m = -1
                    
                    if type(m) is not int:
                        m = m[0]
                    scores.append(m)
                    pos.append((i,j))
    if max_:
        m = max(scores)
    else:
        m = min(scores)
    return [m,pos]
        


player = "x"

while 1:
    pr(board)
    print("\n"+"-"*5)
    try:
        move = minimax(board,"x",c(board))[1][0]
    except:
        move = minimax(board,"x",c(board))[1]
        
    board[move[0]][move[1]] = "x"   #wut?
    
    pr(board)
    print(move)
    ind = int(input("Move : "))
    posx = (ind-1)//3
    posy = (ind-1)%3
    board[posx][posy] = "o"
    
