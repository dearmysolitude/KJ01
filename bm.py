
def bm_match(txt: str, pat: str) -> int:
    skip = [None] * 26

    for pt in range(26):
        skip[pt] = len(pat)
    
    for pt in range(len(pat) - 1):
        skip[ord(pat[pt]) - ord('A')] = len(pat) - pt - 1
    
    pt = len(pat) - 1
    while pt < len(txt):
        pp = len(pat) - 1
        while txt[pt] == pat[pp]:
            if pp == 0:
                return pt
            pt -= 1
            pp -= 1

        pt += skip[ord(txt[pt]) - ord('A')] if skip[ord(txt[pt]) - ord('A')] > len(pat) - pp else len(pat) - pp

    return -1

# if __name__ == '__main__':
#     s1 = input('텍스트를 입력하세요:')
#     s2 = input('패턴을 입력하세요:')

#     idx = bm_match(s1, s2)

#     if idx == -1:
#         print('텍스트 안에 패턴이 존재하지 않습니다.')
#     else:
#         print(f'{idx + 1}번째 문자가 일치합니다.')

#s1 : EAABCBABC
#s2 : CBABC

