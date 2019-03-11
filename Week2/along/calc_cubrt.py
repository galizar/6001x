cube = 342
epsilon = 0.01
guess = 0.
increment = 0.0001
num_guesses = 0

while abs(guess**3 - cube) >= epsilon:
    if guess >= cube:
        break

    guess += increment
    num_guesses += 1

print(f'num of guesses: {num_guesses}')

if abs(guess**3 - cube) >= epsilon:
    print('Failed on cubic root of ', cube)
else:
    print(guess, ' is the cubic root of ', cube)
