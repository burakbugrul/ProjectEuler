#include <cstdio>
#include <iostream>

using namespace std;

const int MAXN = 100000;

long long int mod;
long long int dn[MAXN];
long long int sum[MAXN];

int main(){
	
	scanf("%lld", &mod);
	
	dn[0] = dn[1] = 1LL;
	sum[1] = 1LL;
	
	for( int i=2 ; i<MAXN ; i++ ){
		
		for( int j=1 ; j<=i ; j++ )
			if( j&1 && i - (j * (3LL*j - 1)) / 2 >= 0LL )
				dn[i] = (dn[i] + dn[i - (j * (3*j - 1)) / 2] + dn[i - (j * (3*j + 1)) / 2]) % mod;
			else if( i - (j * (3LL*j - 1)) / 2 >= 0LL )
				dn[i] = (dn[i] - dn[i - (j * (3*j - 1)) / 2] - dn[i - (j * (3*j + 1)) / 2] + mod + mod) % mod;
			else
				break;
		
		if( dn[i] == 0 ){
			printf("%d\n", i);
			break;
		}
	}
	
	return 0;
}
