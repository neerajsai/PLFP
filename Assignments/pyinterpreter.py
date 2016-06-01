from termcolor import colored	

#Calculation Program
def Interpreter_calc(text):
	left=0
        right=0	
	count=0
	if text[0]== '-':
		s=-1
		text=text[1:]
	else:
		s=1
        for i in text:
        	try:
        	        left = (left*10)+float(i)
        	        count=count+1
		except:
			if count == 0:
				left=Values[ord(i)]
				count=count+1
        		break
	flag=1	
	if text[count] == '*':
		flag=0
		if text[count+1] == '*':
			op = '^'
			count = count+1
		else:
			
			op=text[count]
	if flag:
		op=text[count]	
	if count > 0:
        	right=0
        	f=0
        	index=count+1
        	for i in range(index,len(text)):
            		try:
                		right=right*10+float(text[i])
                		f=f+1
            		except:
				if f == 0:	
					right=Values[ord(text[i])]
					f=f+1
                			break
        	left=left*s
	left_value=left
	right_value=right	
	if op == '+': 
		result = left_value + right_value
	elif op == '-': 
		result = left_value - right_value
	elif op == '*': 
		result = left_value * right_value
	elif op == '/': 
		result = left_value / right_value
	elif op == '^': 
		result = left_value ** right_value
	elif op == '%': 
		result = left_value % right_value

	return round(float(result),3)


def main():
  		
    i=1
    while True:
        
	    t='>>> '
            text = raw_input(t)
	    word=text.split(' ')

	    # Writing raw_input in a file and Executing that file
	    if word[0]=="for" or word[0]=="while":
        	    filename="program.py"
		    target=open(filename,'w')
		    target.write(text)
		    target.write("\n")
		    while 1:
			t='   ...: '
	    		t=colored(t,'blue')
			inp = raw_input(t)
			if inp == "":
				break
			target.write(inp)
			target.write("\n")
	    	    target.close()
	    	    execfile('program.py')   
            else:
		
            	text = text.replace(" ", "")
		result=Interpreter_calc(text)
		t=' '
        	print t + str(int(result)) + '\n'
		        		
            i= i+1
    
if __name__ == '__main__':
    main()
