#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <fstream>
#include <map>
#include <set>
#include <math.h>
using namespace std;

int main()
{
    string p, t;
    int i,j,fl=0;
    vector <int> pp;
    vector <int> ans;
    cout << "введите первую строку" << endl;
    getline(cin,t);
    cout << "введите вторую строку" << endl;
    getline(cin,p);
    int thread;
    cout << "введите количество потоков" << endl;
    cin >> thread;
    int n=p.length();
    int m=t.length();
    t=t+t; // циклический сдвиг проверяется при помощи строки, которая конкатенировна с собой же
    pp.push_back(0);
    i=1;
    j=0;
    if(thread>n)
    {
        cout<<"слишком много потоков"<<endl;
        return 0;
    }
    cout<<"построение префикс-функции "<<p<<endl<<endl;
    for(int c=0;c<thread;c++) //цикл по шаблону, разделенный на thread потоков
    {
        cout<<"текущий поток "<<c+1<<endl<<endl;
        while(i!=(c+1)*round(n/thread))  //инициализация префикс-функции
        {
            cout<<"текущие p(i) = p("<<i<<") = "<< p[i] <<", p(j) = p("<<j<<") = "<< p[j] <<endl<<endl;
            if(p[i]==p[j])
            {
                pp.push_back(j+1);
                cout<<"найдено новое значение префикс-функции pp("<<i<<") = "<< j+1<<",так как p(i) = p(j)"<<endl<<endl;
                j++;
                i++;
            }
            else
                {
                if(j==0)
                {
                    pp.push_back(0);
                    i++;
                }
                else
                {
                    j=pp[j-1];
                    cout<<"индекс j перешёл в pp[j-1] = "<<pp[j-1]<<endl<<endl;
                }
            }
        }
        if(c!=thread-1){
        cout<<pp[0];
        for(int l=1;l<pp.size();l++)
        {
            cout<<","<<pp[l];
        }
        cout<<endl<<endl;
        }
    }
    while(p[i]!='\0') //обработка оставшейся части строки (если не делится на равные части)
    {
        if(p[i]==p[j])
        {
            pp.push_back(j+1);
            cout<<"найдено новое значение pp("<<i<<") = "<< j+1<<", так как p(i) = p(j)"<<endl<<endl;
            j++;
            i++;
        }
        else
        {
            if(j==0)
            {
                pp.push_back(0);
                i++;
            }
            else
            {
                j=pp[j-1];
            }
        }
    }
    cout<<"префикс-функция создана:"<<endl<<endl<<pp[0];
    for(int l=1;l<n;l++)
    {
        cout<<","<<pp[l];
    }
    cout<<endl<<endl;

    cout<<"алгоритм кмп"<<endl<<endl;
    i=0;
    j=0;
    for(int c=0;c<thread;c++) //цикл по тексту, разделенный на thread потоков
    {
        cout<<"текущий поток "<<c+1<<endl<<endl;
        while(i!=(c+1)*round((m*2)/thread)) //идем по round(len(b)/thread) символов каждый раз
        {
            cout<<"текущие p(j) = p("<<j<<") = "<< p[j] <<", t(i) = t("<<i<<") = "<< t[i] <<endl<<endl;
            if(p[j]==t[i]) //cовпал ли символ шаблон?
            {
                if(pp.size()-1==j)
                {
                    ans.push_back(i-j); //сохраняем, если шаблон пройден
                    cout<<"найдено новое решение "<<i-j<<", так как дошли до конца шаблона"<<endl<<endl;
                    fl=1;
                    if(j!=0)
                    {
                        cout<<"индекс j перешёл в pp[j-1] = "<<pp[j-1]<<endl<<endl;
                        j=pp[j-1];
                    }
                    else
                        i++;
                }
                else
                {
                    i++;
                    if(p[j+1]!='\0')
                        j++;
                }
            }
            else
            {
                if(j!=0)  //иначе - переход по префикс-функции
                {
                    cout<<"индекс j перешёл в pp[j-1] = "<<pp[j-1]<<endl<<endl;
                    j=pp[j-1];
                }
                else //если в начале шаблона - следующий символ
                {
                    i++;
                }
            }

        }
    }
    while(t[i]!='\0') //обработка оставшейся части строки (если не делится на равные части)
    {
        if(p[j]==t[i])
        {
        if(pp.size()-1==j)
        {
            ans.push_back(i-j);
            cout<<"найдено новое решение "<<i-j<<endl<<endl;
            fl=1;
            if(j!=0)
                j=pp[j-1];
            else
                i++;
        }
        else
        {
        i++;
        if(p[j+1]!='\0')
            j++;
        }
    }
    else
    {
        if(j!=0)
        {
            j=pp[j-1];
        }
        else
        {
            i++;
        }
    }

    }
    if(fl==0 || n!=m)
    {
        cout<<"-1";
        return 0;
    }
    cout<<ans[0];
    return 0;
}
