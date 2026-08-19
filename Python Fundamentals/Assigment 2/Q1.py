# Write a program that takes as input.Using conditional statements,calculate the based on these rules:Q1 salary final tax rate •If salary < 30,000 → 5% •If salary is 30,000 – 70,000 →15% • If salary> 70,000 → 25% 
salary = int(input("enter salary"))

if (salary < 30000):
   taxrate = 0.05
elif (salary <= 70000):
    taxrate = 0.15
else:
    taxrate = 0.25

tax = salary * taxrate
final_salary=salary-tax
print(taxrate)
print(tax) 
print(final_salary)