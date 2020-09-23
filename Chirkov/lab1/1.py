def bt(m, res, n, x, y):
    """
    рекурсивная функция обхода квадрата
    аргументы:
        двумерный массив m (текущее состояние замощения)
        список res (текущие координаты и длины квадратов в замощении)
        число n (сторона обрабатываемой длины квадрата)
        числа x,y (текущие координаты для обработки в цикле далее)
    """
    global t
    global res_min
    global free
    global use
    if use[0]>-(-len(m) // 2): #пропуск лишних вариантов, если есть обязательный квадрат больше ceil(n//2)
        if res:
            a = res[0].split(' ')
            if int(a[0])!=1:
                return
            if int(a[1])!=1:
                return
            if int(a[2])<use[0]:
                return
        if len(res)>1 and len(use)>1:
            a = res[1].split(' ')
            if int(a[2])<use[1]:
                return
    if res_min <= len(res): #пропуск лишних вариантов, относительно промежуточного найденного решения
        return
    if IsPlace(n)+len(res)>=res_min: #пропуск лишних вариантов, относительно возможной оставшейся свободной площади
        return
    if n==1: #единичные квадраты выставляются не в основном цикле, чтобы не было дополнительных итераций
        for i in range(len(m)):
            for j in range(len(m)):
                if(m[i][j]==0):
                    sqnew(m, i, j, n, res)
                    free-=1
    else: 
        if free-n*n>=0: #если есть свободное место
            for i in range(x,x+1):             #проход текущей строки до её конца
                  for j in range(y,len(m)-n+1):
                      if check(m, i, j, n):
                          sqnew(m, i, j, n, res)    
                          free-=n*n
                          if j==len(m)-(n-1):
                              bt(m, res, n, i+1,0)  
                          else:
                              bt(m, res, n, i, j+n-1)
                          sqdel(m, res)        #шаг назад для прохода всех вариантов
                          free+=n*n
                 
            for i in range(x+1,len(m)-n+1):    #проход остальных строк с их начала
                  for j in range(len(m)-n+1):           
                      if check(m, i, j, n):
                          sqnew(m, i, j, n, res)
                          free-=n*n  
                          if j==len(m)-(n-1):
                              bt(m, res, n, i+1,0)  
                          else:
                              bt(m, res, n, i, j+n-1)
                          sqdel(m, res)
                          free+=n*n
        bt(m, res, n-1, 0, 0)
    if free==0:       #проверка на возможный ответ
        if res_min > len(res):
            for s in use: #проверка на обязательные квадраты
                flag=0
                for item in res:
                    a= item.split(' ')
                    if str(s)==a[2]:
                        flag=1
                        break
                if flag==0:
                    break
            if flag==1:  #сохранение ответа
                res_min = len(res)
                t=list(res)
                print(res_min,'квадратов - вероятный ответ:',t)
        
        allsqdel(m, res)
       
def sqnew(m, x, y, n, res): #установка квадрата
    for i in range(n):
        for j in range(n):
            m[x+i][y+j]=1
    res.append(str(x+1)+' '+str(y+1)+' '+str(n))
    
def sqdel(m, res): #удаление квадрата
    if res:
        x = res[len(res)-1].split(' ')
        for i in range(int(x[2])):
            for j in range(int(x[2])):
                m[int(x[0])+i-1][int(x[1])+j-1]=0
        res.pop()
        
def allsqdel(m, res): #удаление всех единичных квадратов
    global free
    while len(res)>0:
        x = res[len(res)-1].split(' ')
        if int(x[2])==1:
            sqdel(m,res)
            free+=1
        else:
            break
    
def printsq(m): #промежуточный вывод двумерного массива
    for i in range(len(m)):
        for j in range(len(m)):
            print(m[i][j],end=' ')
        print("\n")
    print('---------------')
    
def check(m,x,y,n): #проверка можно ли поставить квадрат
    for i in range(n):
        for j in range(n):
            if m[x+i][y+j]!=0:
                return 0       
    return 1

def IsPlace(n): #получение наименьшего количества квадратов, возможных для оставшейся площади
    global free
    answer = 0
    copyfree = free
    while n > 0:
        answer+=copyfree//(n*n)
        copyfree=copyfree%(n*n)
        n=n-1
    return answer

def GetSimple(p): #приведение к простому числу
    for i in range(2, p):
        if p%i==0:
            return i
    return p

print('введите длину квадрата')
c = int(input())
print("введите длины квадрата, которые обязательны для ответа (через пробел), 0 - если неважно")
use = list(map(int,input().split(' ')))
if use == [0]:
    use = [-(-c // 2)]
free=c*c
b = [0] * c
for i in range(c):
    b[i] = [0] * c
n = -(-c // 2)
res = []
t = []
res_min = c*c
use.sort(reverse = True)
summ=0
for s in use:
    summ+=s*s
if summ > c*c:
    print("Нет решения")    
else:
    if use[0]<=n:
        bt(b, res, n, 0, 0)
    else:
        bt(b, res, use[0], 0, 0)
    if res_min!=c*c and t!=[]:
        print(res_min,"квадратов - минимальное замощение")
        #print("координаты и длина квадратов:")
        for x in t:
            q=x.split(' ')
            q[0]=(int(q[0])-1)+1
            q[1]=(int(q[1])-1)+1
            q[2]=int(q[2])
            print(q[0], q[1], q[2])
    else:
        print("Нет решения")
