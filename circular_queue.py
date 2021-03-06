'''
백준 1021번 문제 - 순환하는 큐

##문제
지민이는 N개의 원소를 포함하고 있는 양방향 순환 큐를 가지고 있다.
지민이는 이 큐에서 몇 개의 원소를 뽑아내려고 한다.

지민이는 이 큐에서 다음과 같은 3가지 연산을 수행할 수 있다.

첫 번째 원소를 뽑아낸다.
이 연산을 수행하면, 원래 큐의 원소가 a1, ..., ak이었던 것이 a2, ..., ak와 같이 된다.

왼쪽으로 한 칸 이동시킨다.
이 연산을 수행하면, a1, ..., ak가 a2, ..., ak, a1이 된다.

오른쪽으로 한 칸 이동시킨다.
이 연산을 수행하면, a1, ..., ak가 ak, a1, ..., ak-1이 된다.

큐에 처음에 포함되어 있던 수 N이 주어진다.
그리고 지민이가 뽑아내려고 하는 원소의 위치가 주어진다.
(이 위치는 가장 처음 큐에서의 위치이다.)
이때, 그 원소를 주어진 순서대로 뽑아내는데 드는
2번, 3번 연산의 최솟값을 출력하는 프로그램을 작성하시오.

##입력
첫째 줄에 큐의 크기 N과 뽑아내려고 하는 수의 개수 M이 주어진다.
N은 50보다 작거나 같은 자연수이고, M은 N보다 작거나 같은 자연수이다.
둘째 줄에는 지민이가 뽑아내려고 하는 수의 위치가 순서대로 주어진다.
위치는 1보다 크거나 같고, N보다 작거나 같은 자연수이다.

##출력
첫째 줄에 문제의 정답을 출력한다.
'''

get_input = input()
#get_input = '10 10'
get_input = get_input.split(' ')
len = int(get_input[0])
num = int(get_input[1])

get_input = input()
#get_input = '1 6 3 2 7 9 8 4 10 5'
get_input = get_input.split(' ')
pick = [int(x) for x in get_input]


half = 0
count = 0 # num of second, third operation call
while pick: #until list is empty
    if (pick[0] == 1): # dequeue
        pick.remove(pick[0])
        len -= 1
        if pick: # q is not empty
            pick = [x-1 for x in pick]
            pick = [x+len if (x == 0) else x for x in pick]

    else:
        half = len/2
        left = pick[0] - 1
        right = len - pick[0] + 1
        if (left <= right): # 2번째 연산
            pick = [x-left for x in pick]
            pick = [x+len if (x <= 0) else x for x in pick]
            count += left

        else: # 3번째 연산
            pick = [x+right for x in pick]
            pick = [x-len if (x > len) else x for x in pick]
            count += right


print(count)
