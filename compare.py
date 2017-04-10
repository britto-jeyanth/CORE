import numpy as np

arr2 = np.array(PUT MAZE OUTPUT ARRAY HERE)

print(arr2)
#for row in arr2:
	#print(row)
file = open("maze.txt", 'r')
arr = []
for line in file.readlines():
    arr1 = []
    count = 0
    for c in line:
        if(c.isspace() and (c!="\n")):
            arr1.append(1)
        elif(c!="\n"):
            arr1.append(0)
	count=count+1
	if(count>=33):
		break
    arr.append(arr1)
#print(arr)
arr = np.array(arr)
print(arr)

error = np.mean(arr != arr2)
print(error)





