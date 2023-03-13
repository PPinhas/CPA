#include <iostream>
#include <iomanip>
#include <math.h>
#include <chrono>

using namespace std;

int main(int argc, char** argv) {

    long long n, blockSize;
    
    cout << "Power of 10: ";
    cin >> n;

    cout << "Block Size?: ";
    cin >> blockSize;

    n = pow(10,n);

    blockSize = blockSize>n?n:blockSize;

    bool *primes = new bool[n/2]();

    auto start = chrono::high_resolution_clock::now();

    for(int b = 0; b < n/blockSize; b++) {
        long long k = 3;

        do {
            long long aux = ((b*blockSize / k) + ((b*blockSize % k) != 0)) * k;
            aux = aux%2==0?aux+k:aux;
            long long i = max(k*k, aux);

            for(; i < (b+1)*blockSize; i+=2*k) {
                    primes[i>>1] = true;
            }
            do {
                k += 2;
            } while(k*k < (b+1)*blockSize && primes[k>>1]);
        } while(k * k < (b+1)*blockSize);
    }

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