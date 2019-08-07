#include<iostream>
using namespace std;

int main()
{
	int n,a[10000],i,max=0;
	cout<<"enter number of values:";
	cin>>n;
	cout<<"enter values:";
	for(i=0;i<n;i++)
	{
		cin>>a[i];
	}
	for(i=0;i<n;i++)
	{
		if(a[i]>max)
			max=a[i];
	}
	cout<<"maximum number:"<<max;
}