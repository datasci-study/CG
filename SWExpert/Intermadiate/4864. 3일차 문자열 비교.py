'''두 개의 문자열 str1과 str2가 주어진다. 문자열 str2 안에 str1과 일치하는 부분이 있는지 찾는 프로그램을 만드시오.
예를 들어 두 개의 문자열이 다음과 같이 주어질 때, 첫 문자열이 두번째에 존재하면 1, 존재하지 않으면 0을 출력한다.
ABC
ZZZZZABCZZZZZ
두번째 문자열에 첫번째 문자열과 일치하는 부분이 있으므로 1을 출력.
ABC
ZZZZAZBCZZZZZ
문자열이 일치하지 않으므로 0을 출력.

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  (1≤T≤50)
다음 줄부터 테스트 케이스 별로 길이가 N인 문자열 str1과 길이가 M인 str2가 각각 다른 줄에 주어집니다. (5≤N≤100, 10≤M≤1000, N≤M)

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

[입력 예]
3
XYPV
EOGGXYPVSY
STJJ
HOFSTJPVPP
ZYJZXZTIBSDG
TTXGZYJZXZTIBSDGWQLW

[출력 예]
#1 1
#2 0
#3 1
'''
T = 1
str1 = "ZYJZXZTIBSDG"
str2 = "TTXGZYJZXZTIBSDGWQLW"
N = len(str1)
M = len(str2)
print("N, M : ", N, M)

idx = 0
count = 0
new_index = N-1
while new_index < M: 
    print("new_index : ", new_index)
    print("원래문장 : ", str1)
    print("비교문장 : ", str2)
    print()
    if str2[new_index] != str1[N-1]:
        same_letter = 0
        for i in str1[:-1]:
            if i in str2[(new_index+1 - N):(new_index+1)]:
                print("for원래문장 : ", str1)
                print("for비교문장 : ", str2[(new_index+1 - N):(new_index+1)])
                print("i : ", i)
                idx = N - (str1.index(i)+1)
                print("idx : ", idx)
                print()
                same_letter += 1
            elif same_letter == 0:
                idx = N
        new_index += idx
    else:
        print("str1 : ", str1)
        print("str2 : ", str2[(new_index+1 - N):(new_index+1)])
        if str2[(new_index+1 - N):(new_index+1)] == str1:
            count += 1
        new_index += N
    print("new_index : ", new_index)
    print("count : ", count)
    print()