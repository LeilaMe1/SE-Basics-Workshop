for foo in range(1,21):
    if (foo % 3 == 0):
        print("Fizz")
    if (foo % 5 == 0):
        print("Buzz")
    if ((foo % 3 == 0) and (foo % 5 == 0)):
        print("FizzBuzz")
    if (foo % 3 != 0) and (foo % 5 != 0):
        print(foo)
