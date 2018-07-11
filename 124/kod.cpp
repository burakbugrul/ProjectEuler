#include <cstdio>
#include <iostream>
#include <vector>

using namespace std;

int N, K;
vector<pair<int, int>> rads;

inline int rad( int number ){

    int limit = number, result = 1;

    for( int i=2 ; i*i <= limit ; i++ )
        if( number % i == 0 ){

            result *= i;

            while (number % i == 0 )
                number /= i;
        }
    
    return result*number;
}

int main(){

    scanf("%d%d", &N, &K);
    
    for( int i=1 ; i<=N ; i++ )
        rads.push_back(pair<int, int>(rad(i), i));

    sort(rads.begin(), rads.end());

    printf("%d\n", rads[K-1].second);
    
    return 0;
}
