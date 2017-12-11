from numpy import random

count = 0
random_num = random.randint(1, 9)
print(random_num)

while (True):
    count += 1
    while True:
        try:
            guess = int(input("Enter number in 1 to 9: "))
            break
        except ValueError:
            print("Invalid input!")

    if guess == random_num:
        print("Thats correct, You took {0} guesses.".format(count))
        break
    else:
        if guess > random_num:
            if guess - random_num > 3:
                print("Too high")
            else:
                print("Close!")

        if guess < random_num:
            if random_num - guess > 3:
                print("Too low")

            else:
                print("Close!")
