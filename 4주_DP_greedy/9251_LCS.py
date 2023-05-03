import sys
input = sys.stdin.readline

fstr = input().rstrip()
sstr = input().rstrip()
ln1 = len(fstr)
ln2 = len(sstr)

table = [([0] * (ln2+1)) for _ in range(ln1+1)] #(ln1+1) 개의 행, (ln2+1)개의 열 생성
#0인덱스는 모두 0으로 되어있고, 그 다음 인덱스, 1부터를 str의 몇 번째 글자인지 확인하는 것이다(인덱스 1인 경우 해당 str의 첫번재 글자).

# table[i][j]를 완성하기 위해 table[i-1][j], table[i][j-1], table[i-1][j-1] 셋을 알아야 함.(점화식은 아래 for문을 통해 확인하자)
for i in range(1, ln1+1): #table 범위: 1부터 ln1,2까지 돌면서 해당 테이블을 완성함
    for j in range(1, ln2+1):
        if fstr[i-1] == sstr[j-1]: #str의 인덱스는 0부터 len(f/sstr), i와 j는 table의 인덱스이다.
            table[i][j] = table[i-1][j-1] + 1
        else:
            table[i][j] = max(table[i-1][j], table[i][j-1])

print(table[ln1][ln2])
