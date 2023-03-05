def decimal_to_binary(decimal_num):
    binary_num = bin(decimal_num).replace("0b", "")
    return binary_num
def decimal_to_octal(decimal_num):
    octal_num = oct(decimal_num).replace("0o", "")
    return octal_num
def main():
    decimal_num = int(input("Enter a decimal number: "))
    binary_num = decimal_to_binary(decimal_num)
    octal_num = decimal_to_octal(decimal_num)
    print(f"The binary equivalent of {decimal_num} is: {binary_num}")
    print(f"The octal equivalent of {decimal_num} is: {octal_num}")
main()
