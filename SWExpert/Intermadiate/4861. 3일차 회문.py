'''
ABBA처럼 어느 방향에서 읽어도 같은 문자열을 회문이라 한다. NxN 크기의 글자판에서 길이가 M인 회문을 찾아 출력하는 프로그램을 만드시오.
회문은 1개가 존재하는데, 가로 뿐만 아니라 세로로 찾아질 수도 있다.
예를 들어 N=10, M=10 일 때, 다음과 같이 회문을 찾을 수 있다.

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
다음 줄부터 테스트케이스의 첫 줄에 N과 M이 주어진다. 10≤N≤100, 5≤M≤N
다음 줄부터 N개의 글자를 가진 N개의 줄이 주어진다.

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

[입력 예]
3
10 10
GOFFAKWFSM
OYECRSLDLQ
UJAJQVSYYC
JAEZNNZEAJ
WJAKCGSGCF
QKUDGATDQL
OKGPFPYRKQ
TDCXBMQTIO
UNADRPNETZ
ZATWDEKDQF
10 10
WPMACSIBIK
STWASDCOBQ
AMOUENCSOG
XTIIGBLRCZ
WXVSWXYYVU
CJVAHRZZEM
NDIEBIIMTX
UOOGPQCBIW
OWWATKUEUY
FTMERSSANL
20 13
ECFQBKSYBBOSZQSFBXKI
VBOAIDLYEXYMNGLLIOPP
AIZMTVJBZAWSJEIGAKWB
CABLQKMRFNBINNZSOGNT
NQLMHYUMBOCSZWIOBINM
QJZQPSOMNQELBPLVXNRN
RHMDWPBHDAMWROUFTPYH
FNERUGIFZNLJSSATGFHF
TUIAXPMHFKDLQLNYQBPW
OPIRADJURRDLTDKZGOGA
JHYXHBQTLMMHOOOHMMLT
XXCNJGTXXKUCVOUYNXZR
RMWTQQFHZUIGCJBASNOX
CVODFKWMJSGMFTCSLLWO
EJISQCXLNQHEIXXZSGKG
KGVFJLNNBTVXJLFXPOZA
YUNDJDSSOPRVSLLHGKGZ
OZVTWRYWRFIAIPEYRFFG
ERAPUWPSHHKSWCTBAPXR
FIKQJTQDYLGMMWMEGRUZ

[출력 예]
#1 JAEZNNZEAJ
#2 MWOIVVIOWM
#3 TLMMHOOOHMMLT
'''

'''
3
10 10
GOFFAKWFSA
OYECRSLDLA
UJAJQVSYYB
AAEZNNZEAB
WJAKCGSGCC
QKUDGATDQC
OKGPFPYRKB
TDCXBMQTIB
UNADRPNETA
ZATWDEKDQA
'''
import numpy as np

T = int(input())
for t in range(T):
    N, M = list(map(int, input().split())) # N : 10 by 10,  M : 회문 길이
    grid = [list(map(str, input())) for i in range(N)] # 원래 격자, 가로 검색용
    grid_T = np.transpose(grid).tolist() # 전치 격자, 세로 검색용 (전치행렬로 바꿔 가로 검색의 알고리즘을 그대로 적용)
    # grid_T가 np.ndarray이기 때문에 list로 바꿔줘야 진행이 된다. 이유는 모름. R에 비해 index이 헷갈림
    temp = []

    # 가로 탐색
    for i in range(N):
        for s in range(N-M+1):
            if grid[i][s : M + s] == grid[i][s : M + s][::-1]:
                temp.append(''.join(grid[i][s : M + s]))
                break
    # 세로 탐색
    for i in range(N):
        for s in range(N-M+1):
            if grid_T[i][s : M + s] == grid_T[i][s : M + s][::-1]:
                temp.append(''.join(grid_T[i][s : M + s]))
                break
    print("#{0} {1}".format(t+1, temp[0]))