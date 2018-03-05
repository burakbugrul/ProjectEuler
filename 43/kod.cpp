#include <algorithm>
#include <cstdio>

using namespace std;

long long int to_long_long_int( string number ){
	
	long long int result = 0LL, ten = 1LL;
	
	for( int i=(int)number.size()-1 ; i >= 0 ; i--, ten *= 10LL )
		result += (number[i]-'0') * ten;
	
	return result;
}

long long int substrt_to_long_long_int( string number, int l, int r ){
	
	string tmp = "";
	
	for( int i=l ; i<=r ; i++ )
		tmp += number[i];
	
	return to_long_long_int(tmp);
}

int main(){
	
	long long int result = 0LL;
	
	string number = "1234567890";
	
	do{
		if( substrt_to_long_long_int(number, 1, 3) % 2 == 0 &&
			substrt_to_long_long_int(number, 2, 4) % 3 == 0 && 
			substrt_to_long_long_int(number, 3, 5) % 5 == 0 && 
			substrt_to_long_long_int(number, 4, 6) % 7 == 0 && 
			substrt_to_long_long_int(number, 5, 7) % 11 == 0 && 
			substrt_to_long_long_int(number, 6, 8) % 13 == 0 && 
			substrt_to_long_long_int(number, 7, 9) % 17 == 0 )
				result += to_long_long_int(number);
		
		next_permutation(number.begin(), number.end());
	}while( number != "1234567890" );
	
	printf("%lld\n", result);
	return 0;
}
