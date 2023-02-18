result = bool

# Chaining without using 'AND' operator.
result = 1 > 2 < 3    # Results in AND operation.

# Chaining using 'AND' operator.
result = 1 > 2 and 2 < 3

# OR operation
result = 1 > 2 or 2 < 3

# NOT operation
result = not 1 > 2

# '!' doesn't work with variables or parentheses. We should use NOT keyword.
not result

print(not result)