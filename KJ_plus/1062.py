# 가르침
import sys
input = sys.stdin.readline

N, K = map(int, input().split()) # N <= 50, 자연수, 0 <= K <= 26

learn = [0] * 26
ans = 0
words = [input().rstrip() for _ in range(N)]
words2 = []
# anta tica => 글자가 총 5 개

# 아무 단어도 배울 수 없는 경우
if K < 5:
    print(0)
    exit()
# 모든 단어를 배울 수 있는 경우
elif K == 26:
    print(N)
    exit()

# 있는 단어에서 anta 와 tica를 모두 제거, 중간 글자가 없는 경우 ans =+ 1
for word in words:
    # word = word.strip("anta") 
    # word = word.strip("tica") #  t, i, c, a를 모두 제거한다
    word = word.replace("a", "").replace("n", "").replace("t", "").replace("i", "").replace("c", "")
    words2.append(word)

if K < 5: # K 가 5라면 위에서 ans + 1 한 경우만 출력됨
    print(0)
    exit()
elif K == 26:
    print(N)
    exit()

for char in ('a', 'c', 'i', 'n', 't'):
    learn[ord(char) - ord('a')] = 1
    
def dfs(idx, cnt):
    global ans

    if cnt == K - 5: # 모든 글자를 다 배운 경우
        readcnt = 0
        for word in words2:
            check = True
            for w in word:
                if not learn[ord(w) - ord('a')]:
                    check = False
                    break
            if check:
                readcnt += 1
        ans = max(ans, readcnt)
        return
    
    for i in range(idx, 26): # 아직 다 안배운 경우 dfs로 파고 들어감
        if not learn[i]:
            learn[i] = 1
            dfs(i, cnt + 1)
            learn[i] = 0 # dfs로 파고 들어갔다가 나온 글들은 모두false로 원상복귀

dfs(0, 0)
print(ans)

# if K < 5:
#     print(0)
#     exit()
# else:
#     for word in words:
# 1.
#        word = word.lstrip("anta") # 가장 왼쪽에 있는 단어의 a, n, t, a를 모두 제거한다.
#        word = word.rstrip("tica") # => 가장 오른쪽에 있는 단어의 t, i, c, a를 모두 제거한다
# 2.
#        word = word.replace("anta","") # 가장 왼쪽에 있는 단어의 a, n, t, a를 모두 제거한다.
#        word = word.replace("tica","") # => 가장 오른쪽에 있는 단어의 t, i, c, a를 모두 제거한다
#        print(word)
# 3.     
#        able = word.maketrans({ # 여러 문자열은 사용할 수 없음 ->정규표현식을 통해 이를 피할수 있다: gpt한테 물어봐
#            'anta':'',
#            'tica':''
#        })
#        print(word.translate(table))


    
