#include <stdio.h>
#include <fstream>
#include <iostream>
#include <stdlib.h>
#include <vector>
#include <math.h>

#define SIZE 2000000

int prime[SIZE];



using namespace std;

ofstream save_file;

int isPrime(int num)
{
	int linearstart;

	for (int i=0;i<SIZE;i++)
	{
		if (prime[i]!=0)
		{
			if (num % prime[i] == 0 && num != prime[i])	//is not prime
			{
				return 0;
//				cout<<"should not be here"<<endl;
			}
		}
		else		//donno yet
		{
//			cout<<"should be here"<<endl;
			linearstart=prime[i-1];
			break;
		}
	
	}
	
	
//	printf("start: %d\n", linearstart);
	
	for (int i=linearstart;i<num;i++)
	{
		if (num%i==0 && i!=num)	//is not prime
		{			
			return 0;
		}
	}

	return 1;
}





int main()
{
	
	
	for (int i=0;i<SIZE;i++)
	{
		prime[i]=0;
	}
	
	prime[0]=2;
	
	int count=1;
	
//	cout<<"here"<<endl;
	
	for (long long i=3;i<2000000;i++)	//range of numbers
	{
		int temp = isPrime(i);
		
		if (i%10000==0)
		{
			cout<<i<<endl;
		}
		
		if (temp)		
		{
//			printf("%d: %d\n", i, temp);
			prime[count]=i;
			count++;
			if (count==SIZE)
			{
				cout<<"two million reached"<<endl;
				break;
			}
		}
		
	
	}

/*	
save_file.open("primes.txt");	
	for (int i=0;i<SIZE;i++)
	{
		if (prime[i]!=0)
		{
//			printf("%d: %d\n", i, prime[i]);
			save_file<<prime[i]<<endl;
		}

	}
save_file.close();

*/

long long sum=0;
	for (int i=0;i<SIZE;i++)
	{
		if (prime[i]!=0)
		{
			sum+=prime[i];
		}

	}

printf("sum: %lld", sum);



}



