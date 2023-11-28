## 문제: 기타 레슨
- N개의 강의를 블루레이에 녹화한다: 녹화 시, 강의 순서가 바뀌면 안됨.
- M개의 블루레이에 모든 기타 강의 동영상을 녹화하기로 함. 
- 모든 블루레이의 크기는 동일해아한다: N개 강의를 M개의 그룹 으로 나눈 것은 각각 총 시간이 다르겠지만, 최대 길이의 강의 시간을 지닌 덩어리 만큼을 블루레이의 크기로 해야 모두 녹화할 수 있다. 
- 가능한 블루레이의 크기 중 최소를 구하는 프로그램을 작성하시오.
- 입력시 강의 시간이 작은 것부터 순서대로 입력됨

https://www.acmicpc.net/problem/2343

## 분류

이분탐색, 매개 변수 탐색

## 코멘트

아... 처음 시도했던 코드로는 도저히 답이 나오지 않네. 너무 복잡하게 생각하다보면 생각지도 못한 부분에서 잘못된 처리가 될 수 있다: 알고리즘은 항상 간단하게
```
import sys
input = sys.stdin.readline

nm = input().split()
lectures = list(map(int, input().split()))

N = int(nm[0])
M = int(nm[1])

def canItBe(bluerayTime):
    temp = 0
    cnt = 0

    for lecture in lectures:
        if temp + lecture > bluerayTime:
            temp = lecture
            cnt += 1
            if cnt > M:
                return 2
        else:
            temp += lecture

    if temp:
        cnt += 1
    
    if cnt < M:
        return 1
    elif cnt > M:
        return 2
    else:
        return 3
    
def findValue(lectures):
    a = 0
    minimum = max(lectures)
    maximum = sum(lectures)

    mid = (minimum + maximum) // 2
    a = canItBe(mid)

    while(minimum <= maximum):
        mid = (minimum + maximum) // 2
        a = canItBe(mid)
        if a == 2:
            minimum = mid + 1
        elif a == 1:
            maximum = mid - 1
        elif a == 3:
            return mid

print(findValue(lectures))
```