import numpy as np
class Node:
    def __init__(self,initvalue,initdata):
        self.data = initdata
        self.value= initvalue
        self.lchild = None
        self.rchild = None
    def getData(self):
        return self.data
    def getValue(self):
        return self.value
    def getlChild(self):
        return self.lchild
    def getrChild(self):
        return self.rchild


    def setData(self,newdata):
        self.data = newdata
    def setlChild(self,newdata):
        self.lchild = newdata
    def setrChild(self,newdata):
        self.rchild = newdata
    def setValue(self,newdata):
        self.value = newdata
    
class tree:

    def __init__(self):
        self.head = None
    def isEmpty(self):
        return self.head == None
    def split(self,node,value,array):
    	if(node.getlChild()!=None):
    		self.split(node.getlChild(),value,array)
    		self.split(node.getrChild(),value,array)
    	else:
    		newNode = Node(value,array)
    		node.setlChild(newNode)
    		newNode2 = Node(value,array)
    		node.setrChild(newNode2)


    def add(self,value,array):
        if (self.head == None):
        	newNode = Node(value,array)
        	self.head = newNode
        else:
        	self.split(self.head,value,array)
    def callshow(self):
    	if(self.head!=None):
    		self.show(self.head)
    def show(self,node):
    	print(node.getValue())
    	if(node.getlChild()!=None):
    		self.show(node.getlChild())
    		self.show(node.getrChild())
			
		
         
        



#print ("Enter number of variabes") #number of variables the function is dependent on
#numbers = input()
print ("enter splitting order")
order=list(input())	
numbers = len(order)			      
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
mytree = tree()
for x in order:
	mytree.add(x, output)
mytree.callshow()

