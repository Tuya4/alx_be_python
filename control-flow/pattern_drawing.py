length = int(input("Enter the size of the pattern: "))

# if length < 1:
#     print("Please enter a positive integer.")
    
row = 0

while row < length:
    for col in range(length):
        print("*", end="")
    print()
    row += 1    