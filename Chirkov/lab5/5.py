class AhoNode:  #класс для построения бора (goto - возможные пути, out - шаблоны, удовлетворяющие данной вершине, fail - cуффиксная ссылка) 
    def __init__(self):
        self.goto = {}
        self.out = []
        self.fail = None
        self.isterm = False

def aho_create_bor(patterns): #построение бора вместе с суффиксными и конечными ссылками по массиву строк
    root = AhoNode()
    count = 1
    maxcount1 = 1
    maxcount2 = 0
    for i in range(len(patterns)):  #инициализация структуры бора
        node = root
        for symbol in patterns[i]:
            node = node.goto.setdefault(symbol, AhoNode())
        node.out.append([i,len(patterns[i])])
        node.isterm = True
    queue = []
    for node in root.goto.values(): #добавление в очередь первого уровня ребер
        queue.append(node)
        node.fail = root

    while len(queue) > 0:           #установка суффиксных/конечных ссылок
        rnode = queue.pop(0)
        for key, unode in rnode.goto.items():
            queue.append(unode)
            fnode = rnode.fail
            while fnode is not None and key not in fnode.goto:
                fnode = fnode.fail
            unode.fail = fnode.goto[key] if fnode else root
            unode.out += unode.fail.out
            #if unode.isterm:
                #print(len(unode.out)-1,maxcount2,unode.goto)
            if len(unode.out)-1>maxcount2 and unode.fail.out and unode.isterm:
                maxcount2 = len(unode.out)-1
            elif len(unode.out)>maxcount2 and unode.fail.out:
                maxcount2 = len(unode.out)
                print(unode.out,unode.goto)
    queue = []
    for node in root.goto.values(): 
        queue.append(node)
    while len(queue) > 0:           #подсчёт количества ссылок
        rnode = queue.pop(0)
        if not rnode.isterm:
            for key, unode in rnode.goto.items():
                count = 1
                queue.append(unode)
                fnode = rnode.fail
                while fnode.fail is not None:
                    count+=1
                    fnode = fnode.fail
                        
                if maxcount1<count:
                    maxcount1 = count
        else:
             count = 1
             fnode = rnode.fail
             while fnode.fail is not None:
                count+=1
                fnode = fnode.fail
                    
             if maxcount1<count:
                maxcount1 = count
    print('максимальная длина цепочки суффиксных ссылок равна',maxcount1)
    print('максимальная длина цепочки конечных ссылок равна',maxcount2)
    return root


def aho_find_all(s, root): #реализация алгоритма поиска по строке и бору
    node = root
    ans = []
    for i in range(len(s)):
        while node is not None and s[i] not in node.goto: #пока находимся не в корне и некуда идти по бору
            node = node.fail                              #переход по суффиксной ссылке
            print('перешли по суффиксной ссылке, обрабатывая символ',s[i])
        if node is None:
            node = root
            continue
        node = node.goto[s[i]]                            #шаг вперед
        for pattern in node.out:                          #cохранение ответа
            print('найдено решение на',i - pattern[1] + 2,'символе, шаблон номер',pattern[0]+1)
            ans.append([i - pattern[1] + 2, pattern[0]+1])
    print()
    ans.sort(key=lambda x: (x[0],x[1]))        
    return ans

def print_bor(root):                        #промежуточный вывод бора
    print()
    print('вид бора (обход в ширину)')
    print()
    queue = []
    for key, node in root.goto.items():
        queue.append(node)
    print('можем пойти в следующие вершины из корня',end = ' : ')
    tmp = []
    for key in root.goto.keys():
            print(key, end=' ')
            tmp.append(key)
    print()
    print()
    while len(queue) > 0:
        rnode = queue.pop(0)
        print('можем пойти в следующие вершины из', tmp[0],end=' : ')
        tmp.pop(0)
        if not rnode.goto.items():
            print('-')
        for key, node in rnode.goto.items():
            tmp.append(key)
            print(key, end=' ')
            print()
            print('суффиксная ссылка указывает на возможные переходы',list(rnode.fail.goto.keys()))
            queue.append(node)
            if node.out:
                print(key,end=' терминальная для ')
                for term in node.out:
                    print(term[0]+1,end=' ')
                print()
        if not rnode.goto.items():
            print('суффиксная ссылка указывает на возможные переходы',list(rnode.fail.goto.keys()))
        print()
    
print('введите строку для поиска')
s = input()
print('введите количество шаблонов')
n = int(input())
print('введите шаблоны')
patterns = []
for i in range(n):
    patterns.append(input())
root = aho_create_bor(patterns)
print_bor(root)
for x in aho_find_all(s, root):
    print(x[0],x[1])

