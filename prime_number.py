num = int(input("Enter number to check if it is a prime number - ")
if(num > 1)
    for i in range(2, num):
        if(num % 2 == 0):
            print(num, "is not a prime number")
            print(i, "times" ,num//i, "is" ,num)
        else:
            print(num, "is a prime number")
else:
    print(num, "is not a prime nummber")


