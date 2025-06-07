# Create an array of 5 numbers and print it.
num = [1, 2, 3, 6, 5, 7]
print(num)

# Access the third element of the array.
num1 = (1, 2, 3, 6)
print(num1[2])  # Corrected index to access 3rd element

# Change the second element to 100.
num = [1, 2, 3, 6, 5, 7]
num[1] = 100
print(num)

# Add a number at the end of the array.
num = [1, 2, 3, 6, 5, 7]
num.append(11)
print(num)

# Remove the first element from the array.
num = [1, 2, 3, 6, 5, 7]
num.pop(0)
print(num)

# Print the length of the array.
num = [1, 2, 3, 6, 5, 7]
print(len(num))

# Print all elements using a for loop.
num = [1, 25, 8, 9]
for i in num:
    print(i)

# Check if the number 10 is in the array.
num2 = [1, 2, 6, 8, 9]
if 10 in num2:
    print("yes")
else:
    print("no")

# Sort the array in ascending order.
num = [1, 2, 3, 6, 5, 7]
num.sort()
print(num)

# Reverse the array.
num = [1, 2, 3, 6, 5, 7]
num.reverse()
print(num)
