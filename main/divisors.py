
while(True):
    try:
        num = int(input("Enter number: "))
        break
    except ValueError:
        print("Invalid input!")

divisors = []
for i in range(2, int(num / 2) + 1):
    if num % i == 0:
        divisors.append(i)


print(divisors)