def modPow(k, m):
    x = 1
    t = 10

    while k > 0:
        if k%2 == 1:
            x = x*t%m

        t = t**2%m
        k //= 2

    return x



def A(n):
    n -= 1
    a = 1
    s = 0
    
    while a*3 <= n:
        a *= 3
        s = (s*3 + modPow(n-a, a))%a

    print(a*3-n, "{:.15f}".format(s/a))

A(10**16)

