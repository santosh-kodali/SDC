import numpy as np
def consensus (list1,list2):

	if len(list1) == len(list2):

		output = [[0 for y in range(len(list1))] for x in range(len(list1))]
		for i in range(len(list1)):
			for j in range(len(list2)):
				if i==j:

					output[i][j]=logical_or(list1[j],list2[j])
				else:
					output[i][j]=logical_and(list1[j],list2[j])
		return output

	else:
		return

def logical_and (A,B):
	
	
	if A=='01' and B=='01':
			output1='01'
	if A=='01' and B=='10':
			output1='00'
	if A=='10' and B=='10':
			output1='10'
	if A=='10' and B=='01':
			output1='00'
	if A=='01' and B=='11':
			output1='01'
	if A=='11' and B=='01':
			output1='01'
	if A=='10' and B=='11':
			output1='10'
	if A=='11' and B=='10':
			output1='10'
	if A=='11' and B=='11':
			output1='11'

	return output1


def logical_or (A,B):
	if A=='01' and B=='01':
			output2='01'
	if A=='01' and B=='10':
			output2='11'
	if A=='10' and B=='10':
			output2='10'
	if A=='10' and B=='01':
			output2='11'
	if A=='01' and B=='11':
			output2='11'
	if A=='11' and B=='01':
			output2='11'
	if A=='10' and B=='11':
			output2='11'
	if A=='11' and B=='10':
			output2='11'
	if A=='11' and B=='11':
			output2='11'
	if A=='00' :
			output2=B
	if B=='00':
			output2=A


	return output2

def logical_not (A):
	if A=='01' :
			output2='10'
	if A=='10':
			output2='01'
	if A=='11' :
			output2='00'
	return output2





def cofactor (list1,list2):
	flag=0
	result=[0 for x in range(len(list1))]
	print (result)
	for i in range(len(list1)):
		if logical_and(list1[i],list2[i])=='00':
			flag=1
			print(flag)
			break
	if flag==1:
		return
	else:
		for i in range(len(list1)):
			
			result[i]=logical_or(list1[i],logical_not(list2[i]))
		return result










list1=['01','10','01','01']
list2=['01','10','11','11']

consensus=consensus(list1,list2)
print (consensus)
print(cofactor(list1,list2))