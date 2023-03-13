#include <iostream>
#include <iomanip>
#include <math.h>
#include <chrono>

using namespace std;

int main(int argc, char** argv) {

    long long n;
    
    cout << "Power of 10: ";
    cin >> n;
 
    n = pow(10,n);
    
    bool *primes = new bool[n/2]();
    
    long long k = 3;

    auto start = chrono::high_resolution_clock::now();
    
    do {
        for(long long i = k*k; i < n; i+=2) {
            if(i % k == 0) {
                primes[i>>1] = true;
            }
        }
        do {
            k += 2;
        } while(k*k <= n && primes[k>>1]);
    } while(k * k <= n);

    auto end = chrono::high_resolution_clock::now();
    auto duration_ms = chrono::duration_cast<chrono::milliseconds>(end - start).count();
    cout << "The duration is " << duration_ms << " milliseconds." << endl;
    
    long long nPrimes = 0;
    for(long long i = 0; i < n/2; i++) {
        if(!primes[i]) {
            nPrimes++;   
        }
    }
    cout << "Number of primes: " << nPrimes << endl;

    return 0;
    
    for(long long i = 0; i < n/2; i++) {
        cout << primes[i] << " ";
    }
    cout << endl;
    for(long long i = 0; i < n/2; i++) {
        if(!primes[i]) {
            cout << (i<<1) + 1 << " ";   
        }
    }
    cout << endl;

    return 0;
}