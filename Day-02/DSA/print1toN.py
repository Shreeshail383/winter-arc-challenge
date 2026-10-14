def real(n):
    if n == 0:
        return 
    real(n - 1)
    print(n)

def main():
    n = 4
    real(n)

main()