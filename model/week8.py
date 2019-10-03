import sys
line1=[]
line2=[]
p=0
for line in sys.stdin:
    data=line.strip()
    if data=='':
        break
    p=p+1
    if p==1:
        n=int(data)
    elif p==2: 
       s=data.split(' ')
       for i in s:
           line1.append(int(i))
           
    elif p==3:
       s=data.split(' ')
       for i in s:
           line2.append(int(i))
           
vertical={}
horizontal={}
a=zip(line1,line2)
k=0
for j in a:
    k=k+1
    if j[0]>=j[1]:
        vertical[k]=j[0]-j[1]
    else:
        vertical[k]=j[1]-j[0]
        
k=0
for i in range(0,len(line1)-1):
    k=k+1
    if line1[i]>=line1[i+1]:
        horizontal[k]=line1[i]-line1[i+1]
    else:
        horizontal[k]=line1[i+1]-line1[i]
k=0
for i in range(0,len(line2)-1):
    k=k+1
    if line2[i]>=line2[i+1]:
        horizontal[k]=horizontal[k]+(line2[i]-line2[i+1])
    else:
        horizontal[k]=horizontal[k]+(line2[i+1]-line2[i])

def t(i,horizontal,vertical):
        
        a=horizontal[i]
        b=vertical[i]+vertical[i+1]
        if a>=b:
            return(a)
        else:
            return(b)
two={}
for j in range(1,n):
    two[j]=t(j,horizontal,vertical)    
            

        

def final(n):
      o={}
      o[1]=z+vertical[1]
      o[2]=z+two[1]
      for k in range(3,n+1):
          o[k]=max((o[k-1]+vertical[k]),(o[k-2]+two[k-1]))
       
      return(o[n])
print (final(n)) 
