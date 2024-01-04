# Initial values
x = 5
y = 10

# Print initial values
print("Before switching:")
print("x =", x)
print("y =", y)

# Switching values using a temporary variable
temp = x
x = y
y = temp

# Print values after switching
print("\nAfter switching:")
print("x =", x)
print("y =", y)
