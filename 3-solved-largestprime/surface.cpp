#include <stdio.h>
#include <fstream>
#include <iostream>
#include <stdlib.h>
#include <vector>
#include <math.h>

#define SIZE 50000

long long prime[SIZE];



using namespace std;

ofstream save_file;

bool isPrime(long long num)
{

	
	for (int i=2;i<num;i++)
	{
		if (num%i==0 && i!=num)	//is not prime
		{			
			return false;
		}
	}

	return true;
}





int main()
{

	for(int i=0;i<SIZE;i++)
	{
		prime[i]=0;
	}


	long long num = 600851475143;
	
	long long count=0;
	
	for (long long i=2;i<600851475143;i++)
	{
		if (i==num)
		{
			
			cout<<i<<endl;
			break;
		}
	
		if (isPrime(i) && num % i ==0)
		{
			cout<<i<<endl;
			num=num/i;
			prime[count]=i;
			i=2;
		}
	}
	
	long long temp =0;
	
	for (int i=0;i<SIZE;i++)
	{
		if (prime[i]>temp)
		{
			temp=prime[i];
		}
	} 

	printf("temp: %lld", temp);


}



