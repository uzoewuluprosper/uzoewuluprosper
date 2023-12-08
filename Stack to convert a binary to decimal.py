def binary_to_decimal(binary_number):
    stack = []
    decimal_number = 0
    weight = 0
    
    # Iterate through each bit in the binary number (from right to left)
    for bit in binary_number[::-1]:
        # Convert the bit to an integer
        bit_value = int(bit)
        
        # Multiply the bit by 2 to the power of its weight and add to the decimal number
        decimal_number += bit_value * (2 ** weight)
        
        # Increment the weight for the next bit
        weight += 1
    
    return decimal_number

# Test cases
binary_numbers = ["11000101", "10101010", "11111111", "10000000", "1111100000"]

for binary_number in binary_numbers:
    decimal_result = binary_to_decimal(binary_number)
    print(f"Binary: {binary_number} -> Decimal: {decimal_result}")
