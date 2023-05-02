n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))

# Swap the values using a temporary variable
temp = n1
n1 = n2
n2 = temp

print("Using temp variable")
print("After swapping, the first number is", n1)
print("After swapping, the second number is", n2)

# Swap the swapped-values without using 3rd variable
n1 = n1 + n2
n2 = n1 - n2
n1 = n1 - n2

print("Without using 3rd variable")
print("After swapping, the first number is", n1)
print("After swapping, the second number is", n2)
