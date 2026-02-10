def prime_n(n):
    for i in range(1,n+1):
        if( n%i == 0 ):
            print(n,"is prime")
        else:
            print(n,"is not prime")

n = int(input())
prime_n(n)