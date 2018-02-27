#include <cstdio>

inline int reverse( int number ){
	
	int result = 0;
	
	while( number ){
		result *= 10;
		result += number%10;
		number /= 10;
	}
	
	return result;
}

inline bool check( int number ){
	
	while( number ){
		
		if( !(number & 1) )
			return false;
		
		number /= 10;
	}
	
	return true;
}

int main(){
	
	int N, result = 0;
	
	scanf("%d", &N);
	
	for( int i=1 ; i<N ; i++ )
		if( i % 10 && check(i+reverse(i)) )
			result++;
	
	printf("%d\n", result);
	return 0;
}
