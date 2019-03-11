# improve the precision of a guess

epsilon = 10e-2
y = 14.
guess = y / 2.
num_guesses = 0

while abs(guess*guess - y) >= epsilon:
     num_guesses += 1
     guess = guess - (((guess**2) - y)/(2*guess))

print('Num guesses:', num_guesses)
print(f'square root of {y} is about {guess}')
