EPSILON = 0.01
STEP = 0.1
SQUARE = int(input())
GUESS = 0.0
while GUESS <= SQUARE:
    if abs(GUESS**2-SQUARE) < EPSILON:
        break
    else:
        GUESS += STEP
print(str(GUESS))