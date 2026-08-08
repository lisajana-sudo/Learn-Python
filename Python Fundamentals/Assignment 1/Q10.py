# Take a decimal number as input(like) and out put its :45.78•integer part-45•fractional part-.7
num = float(input("Enter a decimal number: "))

integer_part = int(num)
fractional_part = num - integer_part

print("Integer part -", integer_part)
print("Fractional part -", fractional_part)