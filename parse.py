import numpy as np

print ("Enter number of variabes") #number of variables the function is dependent on
numbers = input()
print ("enter splitting order")
order=list(input())				      
file=open("input.txt","r")        #complements are represented with capital letters
input1=file.readlines()

for i in range(len(input1)) :
	input1[i]=list(input1[i][:-1])
#print(input1)
input1 = np.array(input1,dtype='object')
print(len(input1))
#out_i = [None]*int(numbers)
#output = [out_i]*len(input1)
print(int(numbers))
output = [[0 for x in range(int(numbers))] for y in range(len(input1))] 

print(input1)	
print(output)

for i in range(len(input1)) :
	for j in range(len(order)):
		
		# if order[j]+"'" in input1[i]:     	
		# 	input2[i][j]='01'
		# print (ord(order[j]))	

		# #if [i]='\''
		# 	#i++
		# 	#input[i][j]='10'
		# if chr(ord(order[j]) - 32) in input1[i]:
		# 	input2[i][j]='10'
		
		for k in range(len(input1[i])):

			if	order[j] == input1[i][k]:
				output[i][j] = '01'
				print (output)

				if(k+1<len(input1[i])):
					if input1[i][k+1] == "'":
						output[i][j] = '10'

				break

			if k == len(input1[i])-1:
				output[i][j] = '11'	


print(len(output))
print(output[0])
print(output[1])
#print(input2) 

