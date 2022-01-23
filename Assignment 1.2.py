#1
#LIST METHODS


A=['english','physics','maths']
A.append('computer')    
print(A)


B=['ab','cd','eg']
B.clear() 
print(B)


Y= ['english', 'malayalam', 'hindi']
x = Y.copy()
print(x)


Y= ['english', 'malayalam', 'hindi']
x = Y.count('malayalam')
print(x)

A=['english','physics','maths']
Y= ['english', 'malayalam', 'hindi']
A.extend(Y)
print(A)


Y= ['english', 'malayalam', 'hindi','french']
x = Y.index("french")
print(x)

Y= ['english', 'malayalam', 'hindi','french']
Y.insert(1, 'spanish')
print(Y)

Y= ['english', 'malayalam', 'hindi','french']
Y.pop(2)
print(Y)

Y= ['english', 'malayalam', 'hindi','french']
Y.remove('malayalam')
print(Y)

Y= ['english', 'malayalam', 'hindi','french']
Y.reverse()
print(Y)

Y= ['english', 'malayalam', 'hindi','french']
Y.sort()
print(Y)




#2
#STRING METHODS
txt = "hello world."
x = txt.capitalize()
print (x)


txt = "hello world."
x = txt.casefold()
print (x)

txt = "hello world."
x = txt. center(20)
print (x)

txt = "Nothing is impossible"
x = txt.count("is")
print(x)

txt = "Nothing is impossible"
x = txt.encode()
print(x)


txt = "Nothing is impossible"
x = txt.endswith(".")
print(x)

txt = "Nothing is impossible."
x = txt.endswith(".")
print(x)

txt = "H\te\tl\tl\to\tw\to\tr\tl\td"
x =  txt.expandtabs(2)
print(x)

txt = "she is leaving her home for studies."
x = txt.find("home")
print(x)

txt = "{name}is leaving her home"
print(txt.format(name="lekshmi"))

txt = "she is leaving her home."
x = txt.index("leaving")
print(x)

txt = "helloworld"
x = txt.isalnum()
print(x)

txt="mycaptain"
x=txt.isalpha()
print(x)

txt="my captain"
x=txt.isalpha()
print(x)

txt="my captain"
x=txt.isdecimal()
print(x)

txt = "\u0030" 
x = txt.isdecimal()
print(x)

txt = "\u0030" 
x = txt.isdigit()
print(x)

x="find"
y=x.isidentifier()
print(y)

x="helloworld"
y=x.isascii()
print(y)

x="helloworld"
y=x.islower()
print(y)

x="helloworld"
y=x.isupper()
print(y)

x="my captain"
y=x.isnumeric()
print(y)

x="9846"
y=x.isnumeric()
print(y)

x="my captain"
y=x.isprintable()
print(y)

y = "   "
x = y.isspace()
print(x)

x="my captain"
y=x.istitle()
print(y)

Z = "Hello World"
x = Z.istitle()
print(x)

sub = ("english", "maths", "computer")
txt = "$".join(sub)
print(txt)

txt = "maths"
x = txt.ljust(20)
print(x, "is an interesting subject.")

x="MY CAPTAIN"
y=x.lower()
print(y)

txt = "    maths     "
x = txt.lstrip()
print("of all subjects", x, "is little easy")

nm = "lakshmi"
x = nm.maketrans("a", "e")
print(nm.translate(x))

y= "she is leaving her home"
x = y.partition("is")
print(x)

q = "he like car "
x = q.replace("car", "bike")
print(x)

m = "lekshmi"
n= m.rfind("e")
print(n)

r= "lekshmi"
t= r.rindex("m")
print(t)

txt = "maths"
x = txt.rjust(10)
print(x, "is an interesting subject.")

y= "she is leaving her home"
x = y.rpartition("she")
print(x)

sub = "english,maths,computer"
x = sub.rsplit(", ")
print(x)

txt = "  maths   "
x = txt.rstrip()
print("of all subjects", x, "is little easy")

sub = "she is leaving"
x = sub.rsplit()
print(x)

z = "Thank you for your help\nWelcome "
x = z.splitlines()
print(x)

t = "Hello world."
x = t.startswith("Hello")
print(x)

txt = "  maths   "
x = txt.strip()
print("of all subjects", x, "is little easy")

txt = "Helloworld"
x = txt.swapcase()
print(x)

tx = "Helloworld"
x = tx.title()
print(x)

num='20'
num1=num.zfill(4)
print(num1)


#3
l=[1,2,3,4,5,6]
l1=l[-4]
print(l1)

l1=['a','b','c','d','e']
l2=l1[-2]
print(l2)

Negative indexing is used to display data from the end of the list and 
can  be used to reverse a number without using other functions.



















