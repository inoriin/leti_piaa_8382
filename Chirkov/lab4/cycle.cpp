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
    cout << "??????? ?????? ??????" << endl;
    getline(cin,p);
    cout << "??????? ?????? ??????" << endl;
    getline(cin,t);
    int thread;
    cout << "??????? ?????????? ???????" << endl;
    cin >> thread;
    int n=p.length();
    int m=t.length();
    t=t+t;
    pp.push_back(0);
    i=1;
    j=0;
    if(thread>n)
    {
        cout<<"??????? ????? ???????"<<endl;
        return 0;
    }
    for(int c=0;c<thread;c++)
    {
        cout<<"??????? ????? "<<c+1<<endl;
        while(i!=(c+1)*round(n/thread))
        {
            if(p[i]==p[j])
            {
                pp.push_back(j+1);
                cout<<"??????? ????? ???????? p("<<i<<") = "<< j+1<<endl;
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
        if(c!=thread-1){
        cout<<endl<<pp[0];
        for(int l=1;l<pp.size();l++)
        {
            cout<<","<<pp[l];
        }
        cout<<endl<<endl;
        }
    }
    while(p[i]!='\0')
    {
        if(p[i]==p[j])
        {
            pp.push_back(j+1);
            cout<<"??????? ????? ???????? p("<<i<<") = "<< j+1<<endl;
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
    cout<<endl<<"???????-??????? ???????:"<<endl<<endl<<pp[0];
    for(int l=1;l<n;l++)
    {
        cout<<","<<pp[l];
    }
    cout<<endl;
    i=0;
    j=0;
    for(int c=0;c<thread;c++)
    {
        cout<<endl<<"??????? ????? "<<c+1<<endl;
        while(i!=(c+1)*round(m/thread))
        {
            if(p[j]==t[i])
            {
                if(pp.size()-1==j)
                {
                    ans.push_back(i-j);
                    cout<<"??????? ????? ??????? "<<i-j<<endl;
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
    }  
    while(t[i]!='\0')
    {
        if(p[j]==t[i])
        {
            if(pp.size()-1==j)
            {
                ans.push_back(i-j);
                cout<<"??????? ????? ??????? "<<i-j<<endl;
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
    cout<<endl<<"?????"<<endl<<ans[0];
    for(int u=1;u<ans.size();u++)
    {
        cout<<","<<ans[u];
    }
    return 0;
}