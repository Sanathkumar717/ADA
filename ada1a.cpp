#include<iostream>
using namespace std;

int main()
{
int i,k,a[1000],n,flag;
cout<<"enter num of values:";
cin>>n;
cout<<"enter values of array:";
for(i=0;i<n;i++)
{
cin>>a[i];}

cout<<"enter key:";
cin>>k;
for(i=0;i<n;i++)
{
   if( a[i]==k)
   {
       flag=1;
       break;
   }
   else
    flag=-1;
}
cout<<flag;
}
