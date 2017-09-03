import numpy as np
import copy
from graphviz import Digraph

class Node:
    def __init__(self,initvalue,initlvl,initdata):
        self.data = initdata
        self.value= initvalue
        self.level = initlvl
        self.lchild = None
        self.rchild = None
        self.logic = None
        self.id = None
    def getData(self):
        return self.data
    def getValue(self):
        return self.value
    def getlChild(self):
        return self.lchild
    def getrChild(self):
        return self.rchild
    def getlogic(self):
    	return self.logic
    def getId(self):
    	return self.id
    def getlvl(self):
    	return self.level




    def setData(self,newdata):
        self.data = newdata
    def setlChild(self,newdata):
        self.lchild = newdata
    def setrChild(self,newdata):
        self.rchild = newdata
    def setValue(self,newdata):
        self.value = newdata
    def setLogic(self,newdata):
    	self.logic = newdata
    def setId(self,newdata):
    	self.id = newdata
    def setlvl(self,newdata):
    	self.level = newdata
    
class tree:

    def __init__(self):
        self.head = None
       
    
    def gethead(self):
    	return self.head
    def isEmpty(self):
        return self.head == None
    def split(self,node,value,level,array,counter):
    	if(node.getlChild()!=None):
    		self.split(node.getlChild(),value,level,array,counter)
    		self.split(node.getrChild(),value,level,array,counter)
    	else:
    		
    		newNode = Node(value+str(counter[0]),level,array.copy())
    		node.setlChild(newNode)
    		counter[0] = counter[0] + 1
    	
    		newNode2 = Node(value+str(counter[0]),level,array.copy())
    		node.setrChild(newNode2)
    		counter[0] = counter[0] + 1



    def add(self,value,level,array):
    	counter = [0]
    	if (self.head == None):
        	newNode = Node(value,level,array)
        	self.head = newNode
    	else:
        	self.split(self.head,value,level,array,counter)
    def callshow(self,dot):
    	if(self.head!=None):
    		self.show(self.head,dot)
    def show(self,node,dot):
    	dot.node(node.getValue(),node.getValue()+str(node.getData())+str(node.getlogic())+'\t'+ str(node.getId()))
    	if(node.getlChild() != None):
    		dot.edge(node.getValue(),node.getlChild().getValue())
    		dot.edge(node.getValue(),node.getrChild().getValue())
    	print("Value: %s"%node.getValue())
    	print("Data: %s"%node.getData())
    	if(node.getId() != None):
    		print("Id: %s"%node.getId())
    	if(node.getValue() == 'final'):
    		print("Logic: %s"%node.getlogic())
    	print("\n")
    	if(node.getlChild()!=None):
    		self.show(node.getlChild(),dot)
    		self.show(node.getrChild(),dot)

    def apply(self):
    	if(self.head != None):
    		self.appl(self.head.getlChild(),0)
    		self.appr(self.head.getrChild(),0)
    	else:
    		print("tree is empty")
    def childdatachangel(self,node,index):
    	if(node!=None):
    		temp = node.getData()
    		for x in range(0, len(temp)):
    			if(temp[x][index]=='01'):
    				temp[x][index] = '00'
    			if(temp[x][index]=='10'):
    				temp[x][index] = '11'
    		node.setData(temp)
    		self.childdatachangel(node.getlChild(),index)
    		self.childdatachangel(node.getrChild(),index)

    def childdatachanger(self,node,index):
    	if(node!=None):
    		temp = node.getData()
    		for x in range(0, len(temp)):
    			if(temp[x][index]=='01'):
    				temp[x][index] = '11'
    			if(temp[x][index]=='10'):
    				temp[x][index] = '00'
    		node.setData(temp)
    		self.childdatachanger(node.getlChild(),index)
    		self.childdatachanger(node.getrChild(),index)


    def appl(self,node,index):
    	if(node!= None):

    		temp = node.getData()

    		for x in range(0, len(temp)):
    			if(temp[x][index]=='01'):
    				temp[x][index] = '00'
    			if(temp[x][index]=='10'):
    				temp[x][index] = '11'
    		node.setData(temp)
    		self.childdatachangel(node.getlChild(),index)
    		self.childdatachangel(node.getrChild(),index)

    		
    		self.appl(node.getlChild(),index+1)
    		self.appr(node.getrChild(),index+1)

    def appr(self,node,index):
    	if(node!= None):
    		temp = node.getData()
    		
    		#print(temp)
    		for x in range(0, len(temp)):
    			if(temp[x][index]=='01'):
    				temp[x][index] = '11'
    			if(temp[x][index]=='10'):
    				temp[x][index] = '00'
    		node.setData(temp)
    		self.childdatachanger(node.getlChild(),index)
    		self.childdatachanger(node.getrChild(),index)

    		#print(temp)

    		#self.callshow()
    		self.appl(node.getlChild(),index+1)
    		self.appr(node.getrChild(),index+1)
    def setfinal(self,node):
    	if(node != None):
    		if 'final' in node.getValue():
    			finalcheck = 0
    			for x in node.getData():
    				check = 1
    				for y in x:
    					if y == '00':
    						check = 0
    						break
    				if(check == 1):
    					finalcheck = 1
    			if(finalcheck == 1):
    				node.setLogic(1)
    				node.setId(2)
    			else:
    				node.setLogic(0)
    				node.setId(1)

    		self.setfinal(node.getlChild())
    		self.setfinal(node.getrChild())
    
    def firstloop(self,height):
    	checkarray = []
    	for i in reversed(range(height)):
    	
    		self.idsetting(self.head,i,checkarray)
    	print(checkarray)
    def idsetting(self,node,level,checkarray):
    	if(node != None):
    		self.idsetting(node.getlChild(),level,checkarray)
    		self.idsetting(node.getrChild(),level,checkarray)

    		if(node.getlvl() == level):
    			left = node.getlChild().getId()
    			right = node.getrChild().getId()
    			if(left == right):
    				sum = left
    			else:
    				sum = left + right
    			sum = self.checkarr(checkarray,sum,left,right)
    			node.setId(sum)
    			checkarray.append([sum, left, right])
    def checkarr(self, checkarray,sum,left,right):
    	for x in checkarray:
    		if (sum == x[0]):
    			if (left != x[1] or right != x[2]):
    				final = self.checkarr(checkarray,sum+1,left,right)
    				return final
    			
    	return sum

    			
    		


	    	







    		
  
		
		
         
        


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
output = [[0 for y in range(int(numbers))] for x in range(len(input1))] 

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

output = np.array(output,dtype='object')

dot = Digraph(comment='OBDD')
mytree = tree()
for counter,x in enumerate(order):
	
	mytree.add(x,counter, output)
height = counter +1

mytree.add('final',height, output)


mytree.apply()


mytree.setfinal(mytree.gethead())


mytree.firstloop(height)
mytree.callshow(dot)
dot.render('test-output/OBDD', view=True)