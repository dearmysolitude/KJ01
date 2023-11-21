
### 문제
https://www.acmicpc.net/problem/10815

숫자 카드는 정수 하나가 적혀있는 카드이다. 상근이는 N개를 가지고 있다.
정수 M 개가 주어졌을때, 상근이가 가지고 있는지 구하라.

### 분류
이분 탐색, 해시를 이용한 집합과 맵

### 잡담
전에 만들었던 이분 탐색을 활용. 이분탐색 코드 다시한 번 복습했다.

처음 작성했을때 Runtime오류 발생,
```
for compareCard in comapareCards:
    binary(sangCards, compareCard, 0, len(sangCards)-1, ans)
```
에서 len(sangCards)로 했기 때문에 outofindex오류가 발생한 것. 맨 마지막 요소는 크기-1 이어야 한다.