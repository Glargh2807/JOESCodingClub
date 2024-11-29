name = input(print("What is your name? "))
print("Hello,", name)
exit = bool(False)
total = 0
while (exit == bool(False)):
    numHolder = int(input("Enter an number: "))
    total = total + numHolder
    print(total + numHolder)
    check = input(print("Would you like to add another number? (yes/no)"))
    if (check == "no"):
        exit = bool(True)
print("The sum is", total)

marks = [100,99,97,89,91,59,78,65,32,88]
avg = sum(marks)/len(marks)
print("The average of the marks is", avg)