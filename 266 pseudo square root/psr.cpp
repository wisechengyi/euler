#include <stdio.h>
#include <fstream>
#include <iostream>
#include <stdlib.h>
#include <vector>
#include <math.h>
#include <omp.h>
using namespace std;

int main()
{
	std::cout<<"hello world!"<<std::endl;
	
	int pp[42] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79,
	 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181};
	
	std::vector<int> primes(&pp[0], &pp[0]+42);
	
	double product = 1;
	
	for (unsigned i=0;i<primes.size();i++){
		product *= (double)primes[i];
		std::cout<<product<<std::endl;
	}
	
	std::cout << "product: " << product << std::endl;
	
	double root = sqrt(product);
	
	std::cout << "root: " << root << std::endl;
	

	unsigned long long int max = pow(2,42);
	//unsigned long long int max = 1000000;
	
	std::cout<<"max: "<<max<< std::endl;
	
	double curr_max = 0;
	#pragma omp parallel for 	
	for (unsigned long long int state = 0; state < max; state++ ){
		//cout<< omp_get_thread_num() << " " << state<<endl;
		double curr_prod = 1;
		
		for (int pick = 0; pick < 42; pick++){
			if ( (state >> pick) & 1 ) {
// 				cout<< primes[pick] << " ";
				
				curr_prod *= primes[pick];
			} 
			
			
		
		}
		
		if (curr_prod >= curr_max && curr_prod <= root){
			curr_max = curr_prod;
			cout<<"curr max: "<<curr_prod<<" state: "<<state<<endl;
		}
// 		else{
// 			cout<<endl;
// 		}
// 		
	
	
// 		if (state > 10) {
// 			break;
// 		}
	}
	

}

