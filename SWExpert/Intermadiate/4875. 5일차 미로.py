'''
NxN 크기의 미로에서 출발지에서 목적지에 도착하는 경로가 존재하는지 확인하는 프로그램을 작성하시오. 도착할 수 있으면 1, 아니면 0을 출력한다.
주어진 미로 밖으로는 나갈 수 없다.
다음은 5x5 미로의 예이다.

13101
10101
10101
10101
10021

마지막 줄의 2에서 출발해서 0인 통로를 따라 이동하면 맨 윗줄의 3에 도착할 수 있는지 확인하면 된다.

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
다음 줄부터 테스트 케이스의 별로 미로의 크기 N과 N개의 줄에 걸쳐 미로의 통로와 벽에 대한 정보가 주어진다. 0은 통로, 1은 벽, 2는 출발, 3은 도착이다. 5<=N<=100

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 계산결과를 정수로 출력하거나 또는 ‘error’를 출력한다.

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
4
1131
1101
1101
0002

[출력 예]
#1 1
#2 1
#3 0
'''
def StartPoint(maze):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                return [i, j]

def DFS(x, y):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    if not visited[x][y]:
        visited[x][y] = True

        for ddx, ddy in zip(dx, dy):
            x_p = x + ddx
            y_p = y + ddy
            if  0 <= x_p < N:
                if 0 <= y_p < N:
                    if maze[x_p][y_p] == '3':
                        return True
                    elif not visited[x_p][y_p]:
                        keep = DFS(x_p, y_p)
                        if keep: return True
      
T = int(input())
for t in range(T):
    N = int(input())
    visited = [[False for i in range(N)] for j in range(N)]
    maze = []
    for _ in range(N):
        maze.append(input())
    x, y = StartPoint(maze)

    for i in range(N):
        for j in range(N):
            if maze[i][j] == '1':
                visited[i][j] = True
    if DFS(x, y): result = 1
    else: result = 0

    print("#{0} {1}".format(t+1, result))
    