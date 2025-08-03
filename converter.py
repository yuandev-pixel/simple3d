L=[]
with open("dragon.obj","r") as file:
	lines = file.readlines()
	vf=True
	ff=True
	count=0
	rc=0
	for line in lines:
		if line[0:2]=="v ":
			if vf:
				L.append("---vertstart---\n")
				count+=1
				vf=False
			temp=line.split(" ")
			temp[3]=temp[3].strip()
			L.append("v "+str(float(temp[1])*100)+" "+str(float(temp[2])*100)+" "+str(float(temp[3])*100+300)+" 0 0 0\n")
			count+=1
		if line[0:2]=="f ":
			if ff:
				L.append("---facestart---\n")
				count+=1
				ff=False
			temp=line.split(" ")
			# print(temp)
			print(line)

			tt=[]
			# print(temp)
			# print(len(temp))
			

			print(lines)
			cnt=0
			for vert in temp:
				if cnt>0:
					tt.append(vert.split("/")[0])
				cnt+=1
			L.append("f")
			# print(count)
			for item in tt:
				L[count]=L[count]+" "+str(item)
			L[count]=L[count]+"\n"
			# count+=1
			# if len(temp)>4:
				# count+=1
			count+=1
		rc+=1
	L.append("---textstart---")
print(L)
with open("stupid.mystupidfile","w") as file:
	file.writelines(L)

