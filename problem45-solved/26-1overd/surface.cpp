#include <stdio.h>
#include <fstream>
#include <iostream>
#include <stdlib.h>
#include <vector>
#include <math.h>

using namespace std;

long double proximity_check(long double checkee);

static int repeat = 0;
static int num = 0; 

int main()
{

for (long double i=1; i<1000; i++)
	{
		long double d = 1/i; 
		
		for (long double j=1; j<20; j++)
		{
			long double temp = pow( 10, j) * d - d;
			
			long double diff =  proximity_check(temp) ;
			
//			if (i==2)
//			{
//				cout << "diff: " <<diff<<endl;
//				cout << "temp: " <<temp<<endl;
//			}
			
			
			if ( diff > -.000000001  && diff < .0000000001)
			{
//				printf("%4.0f: %4.10f\n",j, diff) ;
				//printf("%d: %d\n", i, j);
				
				cout<<"i: "<<i<<" j: "<<j<<endl;
				
				if (repeat <= j)
				{
					repeat = j;
					num = i;
					
				}
				
				break;
			}
			
			
			
		}
		
		
		//printf("%4.10f\n",d);	
	}

cout << "num: "<<num<< endl;
cout << "repeat: "<<repeat<< endl;


}

long double proximity_check(long double checkee)
{
	int x = (int) checkee;
	long double temp = (long double ) checkee;
	
	long double diff = checkee - (long double) ((int) checkee);
	 //cout << abs (temp - check)<< end;
	
		
	
	return diff;


}

