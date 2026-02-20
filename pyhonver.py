import pygame
import math

#导入文件
vertex=[]
face=[]
normal=[]
with open("funny.td",'r') as f:
    obj=f.readlines()
for i in range(len(obj)-1):
    obj[i]=obj[i][:-1]
i=0
while obj[i]!="---end---":
    while obj[i]!="---vertstart---":
        i+=1
    i+=1
    while obj[i]!="---normalstart---":
        vertex.append(obj[i])
        i+=1
    i+=1
    while obj[i]!="---facestart---":
        normal.append(obj[i])
        i+=1
    i+=1
    while obj[i]!="---objend---":
        face.append(obj[i])
        i+=1
    i+=1

SCREEN_W=1280
SCREEN_H=720
SCREEN_SIZE = (SCREEN_W,SCREEN_H)
screen=pygame.display.set_mode(SCREEN_SIZE)
running=True

cx=0
cy=0
cz=0
crx=0.1
cry=0
pcx=0
pcy=0
pcz=0
pcrx=0
pcry=0

def avg_to_avgn(avg,n):
    return abs(float(avg.split('|')[n]))

def rx(x,y,z):
    prosses5tmp[1]=x
    prosses5tmp[2]=(scrx*z)+(ccrx*y)
    prosses5tmp[3]=(ccrx*z)-(scrx*y)
def ry(x,y,z):
    prosses5tmp[1]=(ccry*x)-(scry*z)
    prosses5tmp[2]=y
    prosses5tmp[3]=(scry*x)+(ccry*z)

def appendavg():
    avgs.append(f"{j}|{xavg}|{yavg}|{zavg}")
    
def quicksort_n(left,right,n):
    if(left>right):
        return
    base=avgs[left]
    i=left
    j=right
    while(i!=j):
        while avg_to_avgn(avgs[j],n)<=avg_to_avgn(base,n) and i<j:
            j-=1
        while avg_to_avgn(avgs[i],n)>=avg_to_avgn(base,n) and i<j:
            i+=1
        if i<j:
            t=avgs[i]
            avgs[i]=avgs[j]
            avgs[j]=t
    avgs[left]=avgs[i]
    avgs[i]=base
    quicksort_n(left,i-1,n)
    quicksort_n(i+1,right,n)
    return          

def render():
    global scrx,ccrx,scry,ccry,prosses5tmp,avgs,j,xavg,yavg,zavg
    prossesing5ed=[]
    scry=math.sin(math.degrees(cry))
    ccry=math.cos(math.degrees(cry))
    scrx=math.sin(math.degrees(crx))
    ccrx=math.cos(math.degrees(crx))
    for tmp in vertex:
        prosses5tmp=tmp.split(' ')
        print(prosses5tmp)
        prosses5tmp=['v',float(prosses5tmp[1]),float(prosses5tmp[2]),float(prosses5tmp[3])]
        prosses5tmp[1]=prosses5tmp[1]+cx
        prosses5tmp[2]=prosses5tmp[2]+cy
        prosses5tmp[3]=prosses5tmp[3]+cz
        ry(prosses5tmp[1],prosses5tmp[2],prosses5tmp[3])
        rx(prosses5tmp[1],prosses5tmp[2],prosses5tmp[3])
        prossesing5ed.append(f"v {prosses5tmp[1]} {prosses5tmp[2]} {prosses5tmp[3]}")
    
    avgs=[]
    tmp=[]
    tmptmp=[]
    j=0
    for ttmp in face:
        tmp=ttmp.split(' ')
        xavg=0
        yavg=0
        zavg=0
        k=2
        addavg=len(tmp)-1
        for k in range(2,len(tmp)):
            tmptmp=prossesing5ed[int(tmp[k].split('/')[0])-1].split(' ')
            xavg+=float(tmptmp[1])
            yavg+=float(tmptmp[2])
            zavg+=float(tmptmp[3])
            if zavg<0:
                addavg-=1
        xavg/=k-2
        yavg/=k-2
        zavg/=k-2
        appendavg()
        j+=1
    print(avgs)
    quicksort_n(0,len(avgs)-1,3)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    if cx!=pcx or cy!=pcy or cz!=pcz or crx!=pcrx or cry!=pcry:
        render()
        pcx=cx
        pcy=cy
        pcz=cz
        pcrx=crx
        pcry=cry

pygame.quit()
