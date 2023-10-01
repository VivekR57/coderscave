#SIMPLE CALCULATOR
operator=input("ENTER THE OPERATOR (+ - * /):")
Number_1=float(input("ENTER THE FIRST NUMBER:"))
Number_2=float(input("ENTER THE SECOND NUMBER:"))
if operator=="+":
    result=Number_1+Number_2
    print(result)
elif operator=="-":
    result=Number_1-Number_2
    print(result)
elif operator=="*":
    result=Number_1*Number_2
    print(result)
elif operator=="/":
    result=Number_1/Number_2
    print(result)
else:
    print("invalid input")
    