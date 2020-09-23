graph={}
z = input().split(' ')
x = list(map(lambda x: ord(x)-96, z))
for i in range(x[1]):
    graph[chr(i+97)]=[]

while 1:    
    x = input().split(' ')
    if (x==['']):
        break
    if (graph.get(x[0],1)==1):
      graph[x[0]]=[]
      graph[x[0]].append([x[1],float(x[2])])
    else:
      graph[x[0]].append([x[1],float(x[2])])
      
for value in graph.values():
    value.sort(key=lambda x: (x[1],x[0]))

ans=''
while(z[0]!=z[1]):
  if (graph.get(z[0],1)==1):
    graph[z[0]]=[]
  if (graph[z[0]]):
    ans+=z[0]
    z[0]=graph[z[0]][0][0]
    graph[ans[-1:]].pop(0)
  else:
    z[0]=ans[-1:]
    ans=ans[:-1]
ans+=z[1]
print(ans)


