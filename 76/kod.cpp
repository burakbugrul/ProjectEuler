#include <cstdio>
#include <iostream>

using namespace std;

const int MAXN = 110;

int N;

long long int dn[MAXN][MAXN];

long long int f( int n , int limit ){
	
	long long int &result = dn[n][limit];
	
	if( result )
		return result;
	
	if( n <= 1 )
		return result = 1LL;
	
	for( int i=1 ; i<=min(n, limit) ; i++ )
		result = result + f(n-i, i);
	
	return result;
}

int main(){
	
	scanf("%d", &N);
	
	printf("%lld\n", f(N, N)-1);
	
	return 0;
}
