#include <cstdio>

inline int number_of_divisors( int number ){
	
	int count = 0;
	
	for( int i=1 ; i*i <= number ; i++ ){
		if( number % i == 0 )
			count += 2;
		if( i*i == number )
			count--;
	}
	
	return count;
}

int main(){
	
	int limit;
	
	scanf("%d", &limit);
	
	int i=1;
	
	while( number_of_divisors((i*(i+1)) / 2) <= limit )
		i++;
	
	printf("%d %d %d\n", i, (i*(i+1) / 2), number_of_divisors((i*(i+1) / 2)));
	return 0;
}
