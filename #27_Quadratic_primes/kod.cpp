#include <cstdio>

const int MAXN = 10*(1000*1000) + 1001;

int N, A, B, maximum;

bool is_not_prime[MAXN];

inline void sieve(){
	
	is_not_prime[0] = is_not_prime[1] = true;
	
	for( int i=2 ; i<MAXN ; i++ )
		if( !is_not_prime[i] )
			for( int j=2*i ; j<MAXN ; j+=i )
				is_not_prime[j] = true;
}

int main(){
	
	scanf("%d", &N);
	sieve();
	
	for( int a=-N ; a<=N ; a++ )
		for( int b=-N ; b<=N ; b++ ){
			
			int i=0;
			
			while( i*i + a*i + b > 1 && !is_not_prime[i*i + a*i + b] )
				i++;
			
			if( i > maximum ){
				maximum = i;
				A = a;
				B = b;
			}
		}
	
	printf("%d\n", A*B);
	return 0;
}
