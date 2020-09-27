graph={}                #граф - словарь
print("введите начальную и конечную вершину")
z = input().split(' ')
x = list(map(lambda x: ord(x)-96, z))
print("введите ребра и их вес (пустая строка для завершения ввода)")
for i in range(x[1]):
    graph[chr(i+97)]=[] #инициализация начальных вершин

while 1:                #добавление ребер в словарь
    x = input().split(' ')
    if (x==['']):
        break
    if (graph.get(x[0],1)==1):
      graph[x[0]]=[]
      graph[x[0]].append([x[1],float(x[2])])
    else:
      graph[x[0]].append([x[1],float(x[2])])
print("граф до сортировки рёбер")
print(graph)
for value in graph.values(): #сортировка словаря по приоритету
    value.sort(key=lambda x: (x[1],x[0]))
print("граф после сортировки рёбер")  
print(graph)
print()
ans=''
while z[0]!=z[1] and z[0]:
  if (graph.get(z[0],1)==1):
    graph[z[0]]=[]
  if (graph[z[0]]): #выбор вершины с самым дешевым путём
    print('вершина с самым дешёвым путём из',z[0],':',graph[z[0]][0][0])
    print()
    ans+=z[0]
    z[0]=graph[z[0]][0][0]
    graph[ans[-1:]].pop(0)
  else:
    z[0]=ans[-1:]
    print('не найдена вершина для шага вперёд, шаг назад в',z[0])
    print()
    ans=ans[:-1]
if z[0]==z[1]: 
    ans+=z[1]
    print(ans)
else:
    print('нет пути')
