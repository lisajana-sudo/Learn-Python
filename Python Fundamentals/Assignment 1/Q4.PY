# The user enters a string containing a number (e.g.,).Convert it to:"45"• an integer • a float • a string again Print all three value sw
val = input("enter a number ")

convertval = float(val)
print(convertval,type(convertval))

convertval = int(val)
print(convertval,type(convertval))

convertval = str(val)
print(convertval,type(convertval))
