'''
※ SW Expert 아카데미의 문제를 무단 복제하는 것을 금지합니다.
0에서 9까지 숫자가 적힌 N장의 카드가 주어진다.
가장 많은 카드에 적힌 숫자와 카드가 몇 장인지 출력하는 프로그램을 만드시오. 카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력한다. 

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
다음 줄부터 테스트케이스의 첫 줄에 카드 장수 N이 주어진다. ( 5 ≤ N ≤ 100 )
다음 줄에 N개의 숫자 ai가 여백없이 주어진다. (0으로 시작할 수도 있다.)  ( 0 ≤ ai ≤ 9 ) 

[출력] 
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 가장 많은 카드의 숫자와 장 수를 차례로 출력한다.

[입력 예]
3
5
49679
5
08271
10
7797946543

[출력 예]
#1 9 2
#2 8 1
#3 7 3
'''

T = int(input()) # 케이스의 수 T를 생성
if 1<= T <=50: # T의 조건
    result = [[0, 0]]*T # T번의 Test에 대해 가장 많이 등장한 수와 그 빈도를 저장하기 위한 변수 선언

    for j in range(0, T): # T회 반복
        N = int(input()) 

        if 5 <= N <= 100: # N의 조건
            a = [0]*N # N개의 숫자를 받아서 비교해야함
            a = list(map(int, input())) # list(map(int, input()))

            if len(a) == N: # a의 갯수와 N이 일치한다면 진행
                set_a = list(set(a)) # set_a에는 입력받은 값들을 중복없이 저장해 index로 활용 예정
                # set은 순서가 없기때문에 인덱스로 활용 불가, 따라서 list로 활용
                set_a.sort() # 보기 쉽고 처리하기 쉽게 크기 순으로 정렬

                x = [0] * len(set_a) # 인덱스크기만큼 x를 선언, 곧 각 숫자별 빈도가 저장될 변수

                for i in range(0, len(set_a)):
                    # 중복없는 각 숫자별 빈도 저장
                    x[i] = a.count(set_a[i])

                index_freq = [0] * len(x)
                if x.count(max(x)) != 1: # 최빈값을 가지는 숫자가 하나가 아니라면
                    for k in range(len(x)-1, -1, -1): # x의 갯수 이하, -1 초과 까지 -1씩 해가며
                        pass 
                    result[j] = [1, max(x)]
                    print(result[j])
                else:
                    # 결과에 가장 빈도수가 많은 수(max(x))의 위치(x.index)를 반환받아 가장 빈도수 높은 set_a의 숫자를 구함.
                    result[j] = [set_a[x.index(max(x))], max(x)]
                print("a", set_a)
                print("x", x)
                print("set_a[x.index(max(x))]", set_a[x.index(max(x))])

    # 요구 양식에 맞게 출력
    for i in range(1, T+1):
        print("#{0} {1} {2}".format(i, result[i-1][0], result[i-1][1]) )

