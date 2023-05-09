from time import*
from pygame import*
init()
d=display
c=draw.rect
r=Rect
t=l=j=0
while not event.get(256):
 s=d.set_mode((500,300));event.clear();k=key.get_pressed()
 if l:
  if t%66==0:o+=[m:=r(550,y:=time_ns()%11*-20,50,200),m.move(0,300)]
  j+=1;p.y+=min(j,9);c(s,-1,p);t+=1;l=p.collidelist(o+[(0,0,70,300)])==len(o)
  for a in o:a.x-=3;c(s,-1,a)
  if k[32]:j=-8
 else:s.blit(Font().render(str(t),(l:=k[13])and(t:=0),"red"),p:=r(40,90,10,10));o=[]
 o=o[-6:];d.flip();time.wait(33)