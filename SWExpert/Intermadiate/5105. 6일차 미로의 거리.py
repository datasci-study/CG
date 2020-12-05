'''
NxN 크기의 미로에서 출발지 목적지가 주어진다.
이때 최소 몇 개의 칸을 지나면 출발지에서 도착지에 다다를 수 있는지 알아내는 프로그램을 작성하시오.
경로가 있는 경우 출발에서 도착까지 가는데 지나야 하는 최소한의 칸 수를, 경로가 없는 경우 0을 출력한다.
다음은 5x5 미로의 예이다. 1은 벽, 0은 통로를 나타내며 미로 밖으로 벗어나서는 안된다.
13101
10101
10101
10101
10021
마지막 줄의 2에서 출발해서 0인 통로를 따라 이동하면 맨 윗줄의 3에 5개의 칸을 지나 도착할 수 있다.

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
다음 줄부터 테스트 케이스의 별로 미로의 크기 N과 N개의 줄에 걸쳐 미로의 통로와 벽에 대한 정보가 주어진다. 5<=N<=100
0은 통로, 1은 벽, 2는 출발, 3은 도착이다.

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.


[입력 예]
3
5
13101
10101
10101
10101
10021
5
10031
10111
10101
10101
12001
5
00013
01110
21000
01111
00000

[출력]
#1 5
#2 5
#3 0
'''
def startoint(G):
    global N
    for i in range(N):
        for j in range(N):
            if G[i][j] == 2:
                return i, j

def BFS(x, y):
    global dx
    global dy
    global N
    count = 0
    for ddx, ddy in zip(dx, dy):
        x += ddx
        y += ddy
        if (0 <= x <= N) and (0 <= y <= N):
            if visited[x][y] == False:
                count += 1
                visited[x][y] = True
                BFS(x, y)
    return count

T = 1 # int(input())

for t in range(T):
    N = 5 #int(input())
    maze = []
    for _ in range(N):
        maze.append(list(map(int, input())))
    
    visited = [[False for i in range(N)] for j in range(N)]
    
    # 벽(1) 정보를 가진 애들을 이미 방문한 것으로 가정하여 진행
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 1:
                visited[i][j] = True

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    x, y = startoint(maze)
    print("#{0} {1}".format(t+1, BFS(x, y) ))
    


