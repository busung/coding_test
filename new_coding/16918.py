R, C, N = map(int,input().split())

graph = [list(input()) for _ in range(R)]

def find_bomb():

    bomb_list = []

    for x in range(R):
        for y in range(C):
            if graph[x][y] == "O":
                bomb_list.append((x,y))
    return bomb_list

def fire(bomb_list):
    moving_x = [-1,1,0,0]
    moving_y = [0,0,1,-1]

    while len(bomb_list):
        (x,y) = bomb_list.pop()
        graph[x][y] = "."

        for i in range(4):
            n_x = x + moving_x[i]
            n_y = y + moving_y[i]
            if (0 <= n_x < R) and (0 <= n_y < C):
                graph[n_x][n_y] = "."

def setting_bomb():
    for x in range(R):
        for y in range(C):
            graph[x][y] = "O"


for t in range(2,N+1):
    if t % 2 == 0:
        bomb_list = find_bomb()
        setting_bomb()
    else:
        fire(bomb_list)
    
for t in graph:
    for i in t:
        print(i,end="")
    print()