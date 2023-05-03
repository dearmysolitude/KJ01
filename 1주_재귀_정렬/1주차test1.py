numb = int(input()) # base

def funct(original, num, count):
    if num == original and count != 0: #
        print(count)
        return

    first = num % 10
    ten = num // 10
    new = first + ten
    newfirst = new%10
    ans = first * 10 + newfirst
    
    count += 1
    funct(original, ans, count)

funct(numb, numb, 0)