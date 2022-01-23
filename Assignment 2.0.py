#1
#DICTIONARY METHODS

state={'kerala','tamilnadu','gujarat'}
X=state.copy()
print(X)

x = ('1', '2', '3')
y = 0
dictry = dict.fromkeys(x, y)
print(dictry)

state={'kerala':'malayalam','tamilnadu':'tamil','gujarat':'gujarati'}
X=state.get('kerala')
print(X)

state={'kerala':'malayalam','tamilnadu':'tamil','gujarat':'gujarati'}
X=state.items()
print(X)

state={'kerala':'malayalam','tamilnadu':'tamil','gujarat':'gujarati'}
X=state.keys()
print(X)

state={'kerala':'malayalam','tamilnadu':'tamil','gujarat':'gujarati'}
X=state.pop('tamilnadu')
print(X)

state={'kerala':'malayalam','tamilnadu':'tamil','gujarat':'gujarati'}
X=state.popitem()
print(X)

state={'kerala':'malayalam','tamilnadu':'tamil','gujarat':'gujarati'}
X=state.setdefault('kerala','hindi')
print(X)


state={'kerala':'malayalam','tamilnadu':'tamil','gujarat':'gujarati'}
state.update({'bihar':'hindi'})
print(state)


state={'kerala':'malayalam','tamilnadu':'tamil','gujarat':'gujarati'}
X=state.values()
print(X)


#2
#CREATE A SET

set={'python','c','c++'}
print(set)

#3
#sorted function
func=("10","20","30","40")
y=sorted(func,reverse=True)
print(y)

#4
#file extension
filename=input("input the filename:")
f_extns=filename.split(".")[-1]
print ("The extension of the file is: ",f_extns)

#5
#calculator
print("Calculator")
print("1.Add")
print("2.Substract")
print("3.Multiply")
print("4.Divide")

# input choice
ch=int(input("Enter Choice(1-4): "))

if ch==1:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a+b
    print("Sum = ",c)
elif ch==2:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a-b
    print("Difference = ",c)
elif  ch==3:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a*b
    print("Product = ",c)
elif ch==4:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a/b
    print("Quotient = ",c)
else:
    print("Invalid Choice")
    
    


















