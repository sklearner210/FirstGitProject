
num = int(input("Enter number to check if it is a prime number - "))
if num > 1:
    for i in range(2, num):
        if(num % i) == 0:
            print(num, "is not a prime number")
            print(i, "times" ,num//i, "is" ,num)
            break
    else:
            print(num, "is a prime number")
else:
    print(num, "is less than or equal to 1, please choose a number greater than 1")


