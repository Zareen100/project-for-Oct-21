def reverse_bits(num, bit_size):
    reversed_num = 0
    for i in range(bit_size):
        # Extract the last bit of num
        last_bit = num & 1
        # Left shift the reversed_num and add the extracted bit
        reversed_num = (reversed_num << 1) | last_bit
        # Right shift the num to process the next bit
        num >>= 1
    return reversed_num

# Test the function
number = int(input("Enter a number: "))
bit_size = number.bit_length()  # Get the bit length of the number
reversed_number = reverse_bits(number, bit_size)
print(f"Reversed bits number is: {reversed_number}")
