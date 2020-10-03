Name = str(input("Please enter your name -"))
Age = int(input("Please enter your age -"))
Names = []

if Age >= 18:
    print("{Name} as your age is {Age}, you are eligible for booking ticket".format(Name=Name,Age=Age))
Names.append({
    'Name': Name,
    'Age': Age
})
    
for i in Names:
    print(i)
    break

else:
    print("{Name}, Go home and watch POGO".format(Name=Name))