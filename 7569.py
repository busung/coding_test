from collections import deque


M,N,H = map(int,input().split(" "))
graph = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

def bfs(location_list, unripe_cnt):

    que = deque(location_list)
    
    moving_x = [-1,1,0,0,0,0]
    moving_y = [0,0,1,-1,0,0]
    moving_z = [0,0,0,0,1,-1]
    max_days = 1
    
    while len(que):
        (x,y,z) = que.popleft()

        for i in range(6):
            
            n_x = x + moving_x[i]
            n_y = y + moving_y[i]
            n_z = z + moving_z[i]

            if (0 <= n_x < N) and (0 <= n_y < M) and (0 <= n_z < H):
                values = graph[n_z][n_x][n_y]
                if values == 0:
                    graph[n_z][n_x][n_y] = graph[z][x][y] + 1
                    unripe_cnt -= 1
                    max_days = graph[n_z][n_x][n_y]
                    que.append((n_x,n_y,n_z))
    
    if unripe_cnt == 0:
        return max_days - 1
    return -1

location_list = []
unripe_cnt = 0

for x in range(N):
    for y in range(M):
        for z in range(H):
            if graph[z][x][y] == 1:
                location_list.append((x,y,z))
            elif graph[z][x][y] == 0:
                unripe_cnt += 1

ans = bfs(location_list, unripe_cnt)
print(ans)
            
