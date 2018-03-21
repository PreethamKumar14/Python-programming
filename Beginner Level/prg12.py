a=int(raw_input())
if(a<=1000):
        temp=a
	x=0
	while(temp!=0):
        	x=x*10+(temp%10)
        	temp=(temp/10)
	if(x==a):
	  	print("Palindrome")
	else:
		print("Not Palindrome")
else:
	print("no")
