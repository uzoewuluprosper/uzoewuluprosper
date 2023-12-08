def decimal_to_binary(decimal_number):
    stack = []
    
    # Continue dividing the decimal number by 2 and pushing the remainder onto the stack
    while decimal_number > 0:
        remainder = decimal_number % 2
        stack.append(str(remainder))
        decimal_number //= 2
    
    # If the stack is empty, the input decimal number was 0
    if not stack:
        stack.append("0")
    
    # Pop elements from the stack to form the binary representation
    binary_number = ""
    while stack:
        binary_number += stack.pop()
    
    return binary_number

# Test cases
decimal_numbers = [13, 42, 255, 0, 240]

for decimal_number in decimal_numbers:
    binary_result = decimal_to_binary(decimal_number)
    print(f"Decimal: {decimal_number} -> Binary: {binary_result}")
