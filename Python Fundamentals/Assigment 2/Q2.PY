# Write a function that takes two integer a and b and prints  all even numbers between them(inclusiv

def print_even(a, b):
    while(a <= b):
        if a % 2 == 0: 
            print(a)
        a = a + 1

print_even(10, 50)