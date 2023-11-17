def multiply(num_1, num_2):
    if num_2 == 1:
        return num_1
    else:
        return num_1 + multiply(num_1, num_2 - 1)


while True:
    m = int(input("Enter value for m: "))
    n = int(input("Enter value for n: "))

    if m == -1 or n == -1:
        break

    print(multiply(m, n))
