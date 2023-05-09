from time import*
from pygame import*
init()
d=display
c=draw.circle
v=Vector2
s=d.set_mode((500,300))
p=v(40,90)
j=l=1
t=0
o=[]
while not event.get(256)and l:
 event.clear();s.fill(0);j+=1;p.y+=min(j,9)
 if key.get_pressed()[32]:j=-8
 for a in o:
  a.x-=3;c(s,-1,a,50)
  if not(l:=0<p.y<300and(a-p).length()>60):break
 if t%66==0:o+=[v(550,y:=time_ns()%11*10),v(550,y+200)]
 t+=1;o=o[-6:];c(s,-1,p,10);d.flip();time.wait(33)
print("score",time.get_ticks()//1000);quit();input()