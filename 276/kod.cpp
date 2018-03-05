#include <cstdio>
#include <iostream>
#include <vector>

const int MAXN = 1e7+17;

using namespace std;

typedef pair<long long int, int> li;

int N, P;

bool visited[MAXN];

long long int result;
long long int dn[MAXN];

vector<long long int> primes;

inline void sieve( int limit ){
	
	for( long long int i = 2LL ; i<=limit ; i++ ){
		
		if( !visited[i] ){
			
			P++;
			primes.push_back(i);
			
			for( long long int j=i*i ; j<=limit ; j+=i )
				visited[j] = true;
		}
	}
}

long long int power( long long int n, int p ){
	
	long long int res = 1LL;
	
	while(p--)
		res *= n;
	
	return res;
}

void f( vector<li> &prime_count, vector<long long int> &factors, int index, long long int current ){
	
	if( index == (int)prime_count.size() ){
		factors.push_back(current);
		return;
	}
	
	for( int i=0 ; i<=prime_count[index].second ; i++ )
		f(prime_count, factors, index+1, current*power(prime_count[index].first, i));
}

inline void get_factors( long long int n, vector<long long int> &factors ){
	
	vector<li> prime_count;
	
	for( int i=0 ; i<P && n != 1LL ; i++ ) // Finding prime divisors
		if( n%primes[i] == 0 ){
			
			int count = 0;
			long long int prime = primes[i];
			
			while( n%prime == 0 ){
				count++;
				n /= prime;
			}
			
			prime_count.emplace_back(prime, count);
		}
	
	f(prime_count, factors, 0, 1LL);
}

int main(){
	
	scanf("%d", &N);
	
	sieve(N);
	vector<long long int> factors;
	
	for( long long int i=1LL ; i<=N ; i++ ){
		
		dn[i] = (i*i+6)/12 - (i/4)*((i+2)/4); // Alcuin Seuqence
		
		get_factors(i, factors);
		
		for( auto factor : factors )
			if( factor != 1LL && factor != i )
				dn[i] -= dn[factor];
		
		result += dn[i];
		factors.clear();
	}
	
	printf("%lld\n", result);
	return 0;
}
