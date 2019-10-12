
initial_number = 5
print(initial_number)
if initial_number % 2 == 0:
    print("This number its an even")
else:
    print("This number its an odd")

while initial_number > 0:
    initial_number = initial_number - 1
    print(initial_number)
    if initial_number % 2 == 0:
        print("This number its an even")
    else:
        print("This number its an odd")

print("We are done")



