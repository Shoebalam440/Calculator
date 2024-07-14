a=int(input("Enter any number:"))
operator=(input("Choose any operator(+,-,*,/,%)"))
b=int(input("Enter any number:"))
if(operator=="+"):
    print(a+b)
elif(operator=="-"):
    print(a-b)
elif(operator=="*"):
    print(a*b)
elif(operator=="/"):
    print(a/b)
elif(operator=="%"):
    print(a%b)
else:
    print("invalid operator")                