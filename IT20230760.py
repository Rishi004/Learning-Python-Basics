# Python program for implementation of this Quiz

# define function
def Quiz_1(num):
    if num <= 0:
        return 0
    else:
        return num + Quiz_1(num-1)  # recursive


# start loop
while True:
    number = int(input("Enter number: "))  # get user input
    if number == -1:  # check -1 or not
        print("Output: Finished")
        break  # break loop
    else:
        print("Output: " + str(Quiz_1(number)))  # print the output
