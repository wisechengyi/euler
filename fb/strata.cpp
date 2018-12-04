#include <stdio.h>
#include <fstream>
#include <iostream>
#include <stdlib.h>
#include <vector>
// #include <math.h>


#define BUF_SIZE 100000

using namespace std;

int func(int n);

int main(int argc, char *argv[])
{
  

printf("%d\n", func(50));
  
return 0;

}

int func(int n)
{
	if (n==0)
	{
		return 0;
	
	}
	else if (n==1)
	{
		return 1;
	}
	else if (n==2)
	{
		return 1;
		
	}
	else
	{
		return func(n-1) + func(n-2) + func(n-3);
	}
}
