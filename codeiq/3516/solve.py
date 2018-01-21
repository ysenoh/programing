def f(n, a, b):
    return (n-a)*a + (n-b)*b - a*b


def main():
    n, a, b = map(int, input().split())
    print(f(n, a, b))

                        
if __name__ == '__main__':
    main()

                        

