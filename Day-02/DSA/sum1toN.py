def sum(n):
    if n == 0:
        return 0
    return n + sum(n - 1)

def main():
    n = 3
    print(sum(n))

main()