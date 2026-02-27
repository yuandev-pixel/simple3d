import pygame
import math
import random

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
clock=pygame.time.Clock()
color=["#FF0000","#00FF00","#0000FF","#FFFF00","#FF00FF","#00FFFF"]

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
fov=60
sdfscf=10**-10
tangent=math.tan(math.radians(fov/2))

def avg_to_avgn(avg,n):
    return abs(float(avg.split('|')[n]))

def rx(x,y,z):
    r = math.sqrt(y*y+z*z)
    prosses5tmp[1]=x
    prosses5tmp[2]= (scrx*z)+(ccrx*y)
    prosses5tmp[3]= (ccrx*z)-(scrx*y)
def ry(x,y,z):
    r = math.sqrt(x*x + z*z)
    prosses5tmp[1]= (ccry*x)-(scry*z)
    prosses5tmp[2]=y
    prosses5tmp[3]= (scry*x)+(ccry*z)

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
    
def p(x,y,z):
    return (600*(x/(max(1,z)*tangent))+SCREEN_W/2,-600*(y/(max(1,z)*tangent))+SCREEN_H/2)

def render():
    global scrx,ccrx,scry,ccry,prosses5tmp,avgs,j,xavg,yavg,zavg
    prossesing5ed=[]
    scry=math.sin(math.radians(cry))
    ccry=math.cos(math.radians(cry))
    scrx=math.sin(math.radians(crx))
    ccrx=math.cos(math.radians(crx))
    for tmp in vertex:
        prosses5tmp=tmp.split(' ')
      #  print(prosses5tmp)
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
    toberender=[]
    for ttmp in face:
        tmp=ttmp.split(' ')
        xavg=0
        yavg=0
        zavg=0
        k=1
        addavg=len(tmp)-1
        vip=[]
        sz=[]
        for k in range(1,len(tmp)):
            tmptmp=prossesing5ed[int(tmp[k].split('/')[0])-2].split(' ')
            # print(int(tmp[k].split('/')[0])-1)
            xavg+=float(tmptmp[1])
            yavg+=float(tmptmp[2])
            zavg+=float(tmptmp[3])
            if float(tmptmp[3])<=0:
                addavg-=1
                sz.append((False,float(tmptmp[1]),float(tmptmp[2]),float(tmptmp[3])))
            else:
                sz.append((True,float(tmptmp[1]),float(tmptmp[2]),float(tmptmp[3])))
        xavg/=k-2
        yavg/=k-2
        zavg/=k-2
        if addavg==len(tmp)-1:
            appendavg()
            toberender.append(ttmp)
        elif addavg>0:
            size=len(sz)
            for i in range(size):
                if (sz[(i-1)%size][0] or sz[(i+1)%size][0]) and (not sz[i][0]):
                    if sz[(i-1)%size]:
                        vip.append(((i-1)%size,i))
                    if sz[(i+1)%size]:
                        vip.append((i,(i+1)%size))
            for points in vip:
                sxz=(sz[points[0]][3]-sz[points[1]][3])/(sz[points[0]][1]-sz[points[1]][1]+sdfscf)
                kxz=sz[points[1]][3]-sz[points[1]][1]*sxz
                syz=(sz[points[0]][3]-sz[points[1]][3])/(sz[points[0]][2]-sz[points[1]][2]+sdfscf)
                kyz=sz[points[1]][3]-syz*sz[points[1]][2]
                prossesing5ed.append(f"p {-kxz/(sxz+sdfscf)} {-kyz/(syz+sdfscf)} 0")
            s="f"
            vips=0
            for i,point in enumerate(sz):
                if point[0]:
                    s+=f" {int(tmp[k].split('/')[0])}"
                elif sz[(i-1)%size][0] or sz[(i+1)%size][0]:
                    s+=f" {len(prossesing5ed)-vips}"
                    vips-=1
            toberender.append(s)
            
        j+=1
   # print(avgs)
    quicksort_n(0,len(avgs)-1,3)
    s=0
    e=0
    for i in range(len(avgs)):
        if avg_to_avgn(avgs[s],3)!=avg_to_avgn(avgs[e],3):
            quicksort_n(s,e-1,1)
            s=e
        e+=1
    s=0
    e=0
    for i in range(len(avgs)):
        if avg_to_avgn(avgs[s],3)!=avg_to_avgn(avgs[e],3) or avg_to_avgn(avgs[s],1)!=avg_to_avgn(avgs[e],1):
            quicksort_n(s,e-1,2)
            s=e
        e+=1
    j=0
    for avg in avgs:
        tmp=toberender[int(avg.split('|')[0])].split(' ')
        draw=[]
        for k in range(1,len(tmp)):
            tmptmp=prossesing5ed[int(tmp[k].split('/')[0])-1].split(' ')
            draw.append(p(float(tmptmp[1]),float(tmptmp[2]),float(tmptmp[3])))
        pygame.draw.polygon(screen,color[j%6],draw)
       # print(draw)
        j+=1

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    
    press=pygame.key.get_pressed()
    dx=(press[pygame.K_a]-press[pygame.K_d])*3
    dy=(press[pygame.K_z]-press[pygame.K_SPACE])*3
    dz=(press[pygame.K_s]-press[pygame.K_w])*3
    cx+= math.sin(math.radians(90+cry))*dx-math.cos(math.radians(90+cry))*dz
    cy+=dy
    cz+= math.sin(math.radians(90+cry))*dz+math.cos(math.radians(90+cry))*dx
    crx+=(press[pygame.K_DOWN]-press[pygame.K_UP])*1
    cry+=(press[pygame.K_RIGHT]-press[pygame.K_LEFT])*1
    if cx!=pcx or cy!=pcy or cz!=pcz or crx!=pcrx or cry!=pcry:
        screen.fill("#000000")
        render()
        pcx=cx
        pcy=cy
        pcz=cz
        pcrx=crx
        pcry=cry
        print(cx,cy,cz,crx,cry)
    pygame.display.flip()
    
    clock.tick(60)

pygame.quit()
