epsilon = 0.01
k = 1000.0
guess = k/2.0
numGuesses = 0

while abs(guess*guess - k) >= epsilon:
    print(guess)
    guess = guess -(((guess**2) - k)/(2*guess))
    numGuesses += 1
    
print('numGuesses =', numGuesses)
print('Square root of ', k, 'is about ', guess)
