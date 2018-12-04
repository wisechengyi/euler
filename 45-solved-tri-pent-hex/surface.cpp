#include <stdio.h>
#include <fstream>
#include <iostream>
#include <stdlib.h>
#include <vector>
#include <math.h>

using namespace std;




long long tri(long long n)
{
	return n * (n+1)/2;
}

long long pent(long long n)
{
	return n * (3*n-1)/2;
}

long long hex(long long n)
{
	return n * (2*n-1);
}


int casecount[8]={0,0,0,0,0,0,0,0};




int main()
{

	long long t=288;
	long long p=1;
	long long h=1;
	
	while (1)
	{
		long long vtri=tri(t);
		long long vpent=pent(p);
		long long vhex=hex(h);
		
//		printf("tri: %lld, pent: %lld, hex: %lld\n" , vtri,vpent,vhex);
		
//		cout<<"tri: "<<vtri<<" pent: "<<vpent<<" hex: "<<vhex<<endl;
		
		
		if (vtri==vpent && vtri==vhex)
		{
			break;	
		}
		else if(vtri > vpent && vtri>vhex)
		{
			p++;
			h++;
//			cout<<"0"<<endl;
		}
		else if(vtri > vpent && vtri==vhex)
		{
			p++;	
//			cout<<"1"<<endl;
		}
		else if(vtri > vpent && vtri<vhex)
		{
			p++;
//			h--;
//			t++;
//			cout<<"2"<<endl;
		}
		else if(vtri == vpent && vtri>vhex)
		{
			h++;
//			cout<<"3"<<endl;
		}
		else if(vtri == vpent && vtri<vhex)
		{
			p++;
//			cout<<"4"<<endl;
		}
		else if(vtri < vpent && vtri>vhex)
		{
			
			h++;
//			cout<<"5"<<endl;
		}
		else if(vtri < vpent && vtri==vhex)
		{
			t++;
//			p--;
//			cout<<"6"<<endl;
		}
		else if(vtri < vpent && vtri<vhex)
		{
			t++;
//			cout<<"7"<<endl;
		}
		
		
		
		else
		{
			cout<<"here";
		}
		
	
	
	}
	cout<<"final: "<<tri(t)<<" "<<pent(p)<<" "<<hex(h)<<endl;
	
	


}

