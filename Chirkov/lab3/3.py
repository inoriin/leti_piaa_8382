print("введите количество ребер")
n=int(input())
graph={}
print("введите исток и сток (через enter)")
stream = [input(),input()]
edges=[]
print("введите ребра с величиной протекающего потока")
while n>0:                      #добавление ребер в словарь (c учетом обратных)
  x = input().split(' ')
  edges.append(x)
  if graph.get(x[0],1)==1:
    graph[x[0]]=[]
    graph[x[0]].append([x[1],int(x[2])])
  else:
    flag=0
    for item in graph.get(x[0]):#перезаписывание существующего ребра
        if item[0]==x[1]:
            item[1]=int(x[2])
            flag=1
    if flag==0:
        graph[x[0]].append([x[1],int(x[2])])
  if graph.get(x[1],1)==1:
    graph[x[1]]=[]
    graph[x[1]].append([x[0],0])#учет обратного ребра     
  else:
    flag=0
    for item in graph.get(x[1]):
        if item[0]==x[0]:
            flag=1
    if flag==0:
        graph[x[1]].append([x[0],0])  
  n-=1
ans=0
pathexist=1
while pathexist and stream[0]!=stream[1]:
    path=[]
    q=[]
    flags={}
    maxstream=999999
    for key in graph.keys(): #инициализация словаря посещенных ребер
        flags[key]=0
    curr=stream[0]
    for gkey, value in graph.items():
        value.sort(key=lambda x: (abs(ord(gkey)-ord(x[0])),abs(ord('a')-ord(x[0])))) #поиск пути по правилу варианта]
    print()
    print(graph,'- остаточный путь')
    print()
    print('построение пути')
    print()
    while curr!=stream[1]:
        found=0
        for item in graph[curr]:                #обход ребер
          q.append(item)
          q.sort(key=lambda x: (abs(ord(curr)-ord(x[0])),abs(ord('a')-ord(x[0]))))
        print('рассматриваемые рёбра',q,'в вершине',curr)
        print()
        for item in q:
            if flags[item[0]]!=1 and item[1]>0: 
                flags[curr]=1
                path.append(curr)
                print('в путь добавлена вершина',curr,'c потоком',item[1])
                print()
                curr=item[0]
                flags[curr]=1
                found=1         #обновление максимальной величины потока текущего шага
                break
        if curr!=stream[0] and found==0:        #шаг назад, если некуда идти
            flags[curr]=1
            curr=path[-1]
            path.pop()
        elif found==0:                          #если некуда идти в истоке
            pathexist=0
            maxstream=0
            break      
    path.append(stream[1])
    path2=[]
    path2.append(curr)
    curr=stream[1]
    for i in reversed(range(len(path)-1)):
      for item in graph[path[i]]:
          if item[0]==curr and item[1]>0:
            if item[1]<maxstream:
                maxstream=item[1]  
            curr = path[i]
            path2.append(curr)
            break
    ans+=maxstream
    if path!=list(reversed(path2)):
        path=list(reversed(path2))
        print('из пути удалены лишние вершины')
        print()
    if len(path)>1:
      for x in path:
        print(x,end='')
      print()
    for i in range(len(path)-1):     #цикл изменения протекающего потока
        for item in graph[path[i]]:
            if item[0]==path[i+1]:
                item[1]-=maxstream
        for item in graph[path[i+1]]:
            if item[0]==path[i]:
                item[1]+=maxstream
    print()
    print('в остаточном пути изменились рёбра из пути на',maxstream)
print('путей больше нет')
print()
for item in edges:                   #получение фактических величин протекающего потока в ребре с помощью исходной и конечной сети
    for vertice in graph.get(item[0]):
        if vertice[0]==item[1]:
            item[2]=int(item[2])-vertice[1]
print(ans)
edges.sort(key=lambda x: (x[0],x[1]))#отсортированный вывод
for item in edges:
    if item[2]>=0:
        print(item[0],item[1],item[2])
    else:
        print(item[0],item[1],0)

