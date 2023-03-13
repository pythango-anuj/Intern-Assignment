def fizzbuzz(n):
    for i in range(1,n+1):
        if i%3 == 0 and i%5 != 0:
            print("Fizz", end="")
        elif i%3 != 0 and i%5 == 0:
            print("Buzz", end="")
        elif i%3 == 0 and i%5 == 0:
            print("FizzBuzz", end="")
        else:
            print(i, end="")


n = int(input("Enter a natural Number:"))
fizzbuzz(n)