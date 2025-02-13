def calculatesteps( n: int):
    if n == 1 or n == 2:
        return n
    fib = [1, 2]
    curr = [0]
    for i in range(n - 2):
        curr[0] = fib[0] + fib[1]
        fib = [fib[1], curr[0]]
        print(curr,fib)
    return curr[0]

if __name__ == '__main__':
    print(calculatesteps(5))
