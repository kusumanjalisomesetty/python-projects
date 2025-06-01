def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a//b
operation_dict={
    "+":add,
    "-":sub,
    "*":mul,
    "//":div
}


def calculator():
    continue_flag = True
    number1 = int(input("Enter first number"))
    for i in operation_dict:
        print(i)
    while continue_flag:
       oper=input("Pick an Operation")
       number2=int(input("Enter second number"))
       calculator_function=operation_dict[oper]
       result=calculator_function(number1,number2)
       print(f"{number1} {oper} {number2} = {result}")
       output2=input(f"Enter y to continue calculation with {result} or n to exit or x to start a new calculation").lower()
       if output2=='y':
             number1=result
       elif output2=='n':
           continue_flag=False
           print("Bye")
       else:
           continue_flag = False
           calculator()
calculator()




