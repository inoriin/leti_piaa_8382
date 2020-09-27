graph={}                #граф - словарь
print("введите начальную и конечную вершину")
z = input().split(' ')
print("введите ребра и их вес (пустая строка для завершения ввода)")
x = list(map(lambda x: ord(x)-96, z))
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
for keyg, value in graph.items():  #сортировка словаря по приоритету
  value.sort(key=lambda x: (x[1]-ord(x[0])+ord(z[1])))
print("граф после сортировки рёбер")  
print(graph)
print()
q=[]                          #массив открытых вершин
for item in graph[z[0]]:
  q.append([z[0], item[0], item[1], item[1]-ord(item[0])+ord(z[1])])
u=[]                          #массив закрытых вершин
q.sort(key=lambda x: (x[3],x[2],x[1])) #сортировка массива по приоритету

while len(q)!=0:              #алгоритм A*
  if graph.get(q[0][1],1)==1:
          graph[q[0][1]]=[]
  u.append(q[0])              #добавление пройденной вершины
  print("cостояние открытого списка :",q)
  print("в закрытый список добавлена новая вершина", q[0][1],"c минимальным приоритетом", q[0][3],":",u)
  print()
  if(q[0][1]==z[1]):
    break
  for item in graph[q[0][1]]: #обновление открытых вершин
    q.append([q[0][1], item[0], q[0][2]+item[1],q[0][2]+item[1]-ord(item[0])+ord(z[1])])
  if graph[q[0][1]]:
    print("в открытый список добавлены пути из вершины", q[0][1])
    print()
  q.pop(0)                    #удаление пройденной вершины
  q.sort(key=lambda x: (x[3],x[2],x[1],abs(ord(x[0])-ord(x[1])))) #сортировка, чтобы снова на первом месте стоял приоритетный шаг

u.sort(key=lambda x: (x[2],x[0]))
print("отсортированный массив закрытых вершин, формат: [начальная вершина, конечная вершина, стоимость пути, приоритет]")
print(u)
print()
answer=''  
now=z[1]
while now!=z[0]:              #формирование ответа по массиву закрытых вершин
  for x in u:
    if x[1]==now:
      answer+=now
      now=x[0]
      break
answer+=now
answer=answer[::-1]
print("oтвет:", answer)
