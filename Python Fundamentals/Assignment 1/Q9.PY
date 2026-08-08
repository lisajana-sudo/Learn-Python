# Principal(P),Rate(R),Time(T).Convert all to FLOAT and compute  Simple interest:I=(P∗R∗T)/100
P = input("Enter a number: ")
R = input("enter a number: ")
T = input("enter a number: ")
convert_p = float(P)
convert_R = float(R)
convert_T = float(T)
simpleinterest = (convert_p*convert_R*convert_T)/100
print(simpleinterest)                

