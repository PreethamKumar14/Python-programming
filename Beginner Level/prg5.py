print("Enter 3 numbers:")
a=input()
b=input()
c=input()
if isinstance(a,str) or isinstance(b,str) or isinstance(c,str):
    if(a>='a' and a<='z' and b>='a' and b<='z' and c>='a' and c<='z'):
        print("Invalid Input")
    else:
        a=int(a)
	b=int(b)
	c=int(c)
	if(a>b and a>c):
	    print(a)
        elif(b>a and b>c):
	    print(b)
	else:
	    print(c)
