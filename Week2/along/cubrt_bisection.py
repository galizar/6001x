x = 27
epsilon = 0.01
num_guesses = 0
low = 1.
high = x
ans = (high + low) / 2.

while abs(ans**2 - x) >= epsilon:
    print(f'low = {str(low)} high = {str(high)} ans = {str(ans)}')
    num_guesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low) / 2.

print(f'num_guesses = {str(num_guesses)}')
print(f'{str(ans)} is close to square root of {str(x)}')
