print("USING Herons Algorthim TO GUESS SquareRoot of  A number ")
x = float(input("Enter the number to guess its square root:\n\tX = "))
guess = x / 2
e = 10 ** -12

while abs((guess ** 2) - x) >= e:
    guess = (guess + x / guess) / 2

print(guess)
