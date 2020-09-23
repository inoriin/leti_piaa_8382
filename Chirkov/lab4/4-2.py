def kmp(a,b,thread): #алгоритм Кнута-Морриса-Пратта, аргументы - шаблон, текст, количество потоков
    n=len(a)
    b+=b
    m=len(b)
    ans=[]
    p=[0]*n
    j=0
    i=1
    print()
    print('построение префикс-функции')
    print()
    for ptr in range(thread-1): #цикл по шаблону, разделенный на thread потоков
        print('текущий поток',ptr+1)
        while i!=(ptr+1)*(round(n//thread)):      #инициализация префикс-функции
            if a[i]==a[j]:
                print('найдено новое значение p(',i,')=',j+1,sep='')
                p[i]=j+1
                i+=1
                j+=1
            elif j==0:
                p[i]=0
                i+=1
            else:
                j=p[j-1]
        print(p)
        print()
    print('текущий поток',thread)
    while i!=n:     
        if a[i]==a[j]:
            print('найдено новое значение p(',i,')=',j+1,sep='')
            p[i]=j+1
            i+=1
            j+=1
        elif j==0:
            p[i]=0
            i+=1
        else:
            j=p[j-1]
    print()
    print('префикс-функция создана',p)
    k=0
    l=0
    print()
    for i in range(thread-1): #цикл по тексту, разделенный на thread потоков
        print('текущий поток',i+1)
        while k!=(i+1)*(round(m//thread)): #идем по round(len(b)/thread) символов каждый раз
            if b[k]==a[l]:              #cовпал ли символ шаблон?
                if l==n-1:
                    ans.append(k-l)     #сохраняем, если шаблон пройден
                    print('найдено новое решение',ans[-1])
                    if l!=0:
                        l=p[l-1]
                    else:
                        k+=1
                else:
                    k+=1
                    if l<n-1:
                        l+=1
            elif l==0:                  #если в начале шаблона - следующий символ
                k+=1
            else:                       #иначе - переход по префикс-функции
                l=p[l-1]
        print()
    print('текущий поток',thread)    
    while k!=m: #обработка оставшейся части слова (если не делится на равные части)
        if b[k]==a[l]:
            if l==n-1:
                ans.append(k-l)
                print('найдено новое решение',ans[-1])
                if l!=0:
                    l=p[l-1]
                else:
                    k+=1
            else:
                k+=1
                if l<n-1:
                    l+=1
        elif l==0:
            k+=1
        else:
            l=p[l-1]
    print()   
    if ans==[]: #вывод
        print(-1)
    else:
        print(ans[0])
print('введите первую строку')
a=input()
print('введите вторую строку')
b=input()
print('введите количество потоков')
thread=int(input())
if thread>len(a):
    print('слишком много потоков')
elif len(a)!=len(b):
    print('длины строк не равны')
else:   
    kmp(a,b,thread)
