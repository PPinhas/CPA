#include <iostream>
#include <iomanip>
#include <math.h>

using namespace std;

int main (int argc, char *argv[])
{
    long long n;
    cout << "Power of 10: ";
    cin >> n;
    n = pow(10,n);
    bool *primes = new bool[n];
    long long k = 3;

    do
    {
        for (long long j = k*k ; j<n ; j+=2)
        {   
            if(j % k == 0){primes[j] = true;}
        } 
        
        do
        {
            k+=2;
        }while (k*k <= n && primes[k]);
        
    } while (k*k <= n);
    
    cout << "1 ";
    cout << "2 ";
    for (int i=3; i<n; i+=2)
        if (!primes[i]){
            cout << i << " ";
        }
}