import math
L=[]
filename="funny"
with open(filename+".obj","r") as file:
	lines = file.readlines()
	vf=True
	vnf=True
	ff=True
	count=0
	rc=0
	of=True
	for line in lines:
		if line[0:2]=="o ":
			if not of:
				L.append("---objend---\n")
			L.append("---obj---\n")
			of=False
			vf=True
			vnf=True
			ff=True
		if line[0:2]=="v ":
			if vf:
				L.append("---vertstart---\n")
				count+=1
				vf=False
			temp=line.split(" ")
			temp[3]=temp[3].strip()
			L.append("v "+str(float(temp[1])*100)+" "+str(float(temp[2])*100)+" "+str(0-float(temp[3])*100+300)+"\n")
			count+=1
		if line[0:3]=="vn ":
			if vnf:
				L.append("---normalstart---\n")
				count+=1
				vnf=False
			L.append(line)
			count+=1

		if line[0:2]=="f ":
			if ff:
				L.append("---facestart---\n")
				count+=1
				ff=False
			L.append(line)
		rc+=1
# print(L)
L.append("---objend---\n---end---")
with open(filename+".td","w") as file:
	file.writelines(L)
