비트마스크를 사용하여 26개 글자를 가지고 dfs로 들어가, 제일 큰 숫자의 ans를 찾아내는 방식으로 풀 수 있다.(브루트 포스)

```
if K < 5:
    print(0)
    exit()
else:
    for word in words:
1.
       word = word.lstrip("anta") # 가장 왼쪽에 있는 단어의 a, n, t, a를 모두 제거한다.
       word = word.rstrip("tica") # => 가장 오른쪽에 있는 단어의 t, i, c, a를 모두 제거한다 
2.
       word = word.replace("anta","") # 가장 왼쪽에 있는 단어의 a, n, t, a를 모두 제거한다.
       word = word.replace("tica","") # => 가장 오른쪽에 있는 단어의 t, i, c, a를 모두 제거한다
       print(word)
3.     
       able = word.maketrans({ # 여러 문자열은 사용할 수 없음 ->정규표현식을 통해 이를 피할수 있다: gpt한테 물어봐
           'anta':'',
           'tica':''
       })
       print(word.translate(table))
4. word 내 모든 글자를 제거
       word = word.strip("antic")
```