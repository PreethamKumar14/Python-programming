x=raw_input()
if isinstance(x,str):
    if(x>='a' and x<='z'):
		    print("Invalid Input")
	  else:
		    temp=int(x)
		    if(temp>=0):
			      c=0
			      while(temp <> 0):
				        temp=temp/10
				        c=c+1
			      print(c)
		    else:
			      c=0
			      a=abs(temp)
			      while(a <> 0):
				        a=a/10
				        c=c+1
			      print c
