def validate_binary(num):
    return all(c in '01' for c in num)

# one_complement
def one_complement(num):
    complement = ""
    for digit in num:
        complement += '1' if digit == '0' else '0'
    return complement

#two_complement
def two_complement(num):
        one_comp = one_complement(num)
        two_comp = ''
        carry = 1

        for bit in reversed(one_comp):
            if bit == '1' and carry == 1:
                two_comp = '0' + two_comp
            elif bit == '0' and carry == 1:
                two_comp = '1' + two_comp
                carry = 0
            else:
                two_comp = bit + two_comp

        return two_comp
#binary_addition
def binary_addition(num1, num2) :
# Initialise result variables
    result = ""
    carry = 0

    # Ensure both binary strings are of equal length
    max_length = max(len(num1), len(num2))
    num1 = num1.zfill(max_length)
    num2 = num2.zfill(max_length)

    # Add each bit of binary1 and binary2, considering carry
    for i in range(max_length - 1, -1, -1):
        bit1 = int(num1[i])
        bit2 = int(num2[i])

        temp_sum = bit1 + bit2 + carry
        carry = 1 if temp_sum > 1 else 0

        result = str(temp_sum % 2) + result


    # Add the final carry, if any
    if carry != 0:
       result = str(carry) + result
    return result

#binary_subtraction
def binary_subtraction(num1, num2):
    # Calculate the maximum length of the input strings
    max_length = max(len(num1), len(num2))

    # Expand the input strings to have equal lengths
    num1 = num1.zfill(max_length)
    num2 = num2.zfill(max_length)

    # Initialize variables to store result and borrow
    result = ''
    borrow = 0

    # Perform binary subtraction
    for i in range(max_length):
        digit_num1 = int(num1[-i - 1])
        digit_num2 = int(num2[-i - 1])
        total = digit_num1 - digit_num2 - borrow
        result = str(total % 2) + result
        borrow = 0
        if total < 0:
            borrow = 1

    return result.lstrip('0') or '0'

def binary_calculator():
    global choice, num1
    while True:
        try:
            print("\nBinary Calculator")
            print("A) Insert new numbers")
            print("B) Exit")
            choice = input("Please select a valid choice: ").upper()

            if choice == 'A':
                while True:
                    num1 = input("Please insert the first number: ")

                    if validate_binary(num1) :
                        break
                    else:
                        print("Please insert valid binary numbers.")
            elif choice == 'B':
                break
            else:
                print("Please select a valid choice.")

        except ValueError:
            print("Please enter a valid number.")

        if choice == 'A':
            while True:
                print("\nPlease select the operation")
                print("A) Compute one's complement")
                print("B) Compute two's complement")
                print("C) Addition")
                print("D) Subtraction")
                operation = input("Please select a valid operation: ").upper()

                if operation == 'A':
                    result = one_complement(num1)
                    print("The one's complement of the first number is:", result)
                elif operation == 'B':
                    result = two_complement(num1)
                    print("The two's complement of the first number is:", result)
                elif operation == 'C':
                    while True:
                        num2 = input("Enter the second  number: ")
                        if validate_binary(num2):
                            break
                        print("Please insert a valid binary number.")
                    result = binary_addition(num1, num2)
                    print("The sum of the two numbers is:", result)
                elif operation == 'D':
                    while True:
                        num2 = input("Enter the second  number: ")
                        if validate_binary(num2):
                            break
                        print("Please insert a valid binary number.")
                    result = binary_subtraction(num1, num2)
                    print("The difference of the two numbers is:", result)
                else:
                    print("Please select a valid operation.")

                # Display the menu again to allow the user to choose again
                if input("Press Enter to continue or type 'q' to quit: ").lower() == 'q':
                    break

binary_calculator()