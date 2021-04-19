n=97
ng=0
print("You have only 10 guesses")

while ng<=10:
    m=int(input("Enter the number"))
    if m<n:
        print("Your number is less than the real one")
    elif m>n:
        print("Your number is greater than the real one")
    else:
        print("You WON the game : you guesses the right number")
        break
    ng=ng+1
    if ng>9:
        print("GAME over ")