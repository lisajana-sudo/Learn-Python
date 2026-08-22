# Write a function that print the digit  of a number n.
def print_digit(n):
    for digit in str(n):
        print(digit)

def print_dig_int(num):
    divisor = 1

    while num // divisor >= 10:
        divisor = divisor * 10

    while divisor > 0:
        print(num // divisor)
        num = num % divisor
        divisor = divisor // 10

num = int(input("enter a number:"))

print_dig_int(num)