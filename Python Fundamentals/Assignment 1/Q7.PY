# Ask the user for a temperature in Celsius (string input).Convert it to,then calculate and pr int temperature in Fahrenheit.
temparature = input("enter temparature in celsius: ")
convert_temparature = float(temparature)
print(convert_temparature)

fahrenheit_temp=(convert_temparature * (9/5)+32)
print(fahrenheit_temp)