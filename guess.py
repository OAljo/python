secret_number=9
chance=0
while chance<3:
    guess=int(input(" Enter your guess : "))
    chance+=1
    if guess==secret_number:
        print('you won ')
        break
else:
    print(" you failed ")