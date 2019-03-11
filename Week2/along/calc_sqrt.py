# if i remember correctly this is an algorithm for calculating (or approximating?) the
# square root of a number
ans = 0
neg_flag = False
x = int(input('Please enter an integer: '))
if x < 0:
    neg_flag = True

while ans**2 < x:
    ans = ans + 1

if ans**2 == x:
    print(f'square root of {x} is {ans}')
else:
    print(x, ' is not a perfect square')
    if neg_flag:
        print(f'Can not compute square of negative integer. Did you mean {-x}?')
