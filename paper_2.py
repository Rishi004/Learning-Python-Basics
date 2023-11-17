def fibonacci(num):
    if num <= 1:
        return num

    return fibonacci(num - 1) + fibonacci(num - 2)


while True:
    n = int(input("Enter number: "))
    if n == -1:
        break

    print(fibonacci(n))
