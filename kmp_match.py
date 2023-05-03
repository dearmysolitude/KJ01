def kmp_match(txt: str, pat: str) -> int:
    pt = 1
    pp = 0
    skip = [0] * (len(pat) + 1)
    skip[pt] = 0

    while pt != len(pat):
        if pat[pt] == pat[pp]:
            pt += 1
            pp += 1
            skip[pt] = pp
        elif pp == 0:
            pt += 1
            skip[pt] = pp
        else:
            pp = skip[pp]
    
    print("skip : " + ", ".join(map(str, skip)))

    pt = pp = 0
    count = 0
    while pt != len(txt) and pp != len(pat):
        if txt[pt] == pat[pp]:
            pt += 1
            pp += 1
        elif pp == 0:
            pt += 1
        else:
            pp = skip[pp]
            count += 1

    print("count: " + str(count))

    return pt - pp if pp == len(pat) else -1

# if __name__ == '__main__':
#     s1 = input('텍스트를 입력하세요.: ')
#     s2 = input('패턴을 입력하세요.: ')
#     idx = kmp_match(s1, s2)

#     if idx == -1:
#         print('텍스트 안에 패턴이 존재하지 않습니다.')
#     else:
#         print(f'{(idx+1)}번째 문자가 일치합니다.')

# txt = abcabgabcaabcabcabgabcaef
# pat = abcabgabcae

# skip 배열과 count 값이 어떻게 될지 맞춰 보시면 됩니다.