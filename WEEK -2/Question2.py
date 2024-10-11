#Write a program that demonstrates the use of assignment operators with variables.

# Initializing variables
a = 10
b = 5

# Addition assignment (+=)
print(f"Initial value of a: {a}")
a += b  
print(f"After a += b, value of a: {a}")

# Subtraction assignment (-=)
a -= b  
print(f"After a -= b, value of a: {a}")

# Multiplication assignment (*=)
a *= b  
print(f"After a *= b, value of a: {a}")

# Division assignment (/=)
a /= b  
print(f"After a /= b, value of a: {a}")

# Modulus assignment (%=)
a %= b  
print(f"After a %= b, value of a: {a}")

# Exponentiation assignment (**=)
a = 2  # Re-assigning a value to a
b = 3  # Re-assigning b value
a **= b  # Equivalent to a = a ** b
print(f"After a **= b, value of a: {a}")

# Floor division assignment (//=)
a //= b  # Equivalent to a = a // b
print(f"After a //= b, value of a: {a}")
