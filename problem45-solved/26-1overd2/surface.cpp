#include <stdio.h>
#include <fstream>
#include <iostream>
#include <stdlib.h>
#include <vector>
#include <math.h>

using namespace std;


int main()
{
	double x= 0.0002/5;
	
	char buf[100];
	
	sprintf(buf, "%4.16f", x);
	
	printf("%s\n", buf);


}

