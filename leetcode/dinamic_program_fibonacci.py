"""Dinnamic program: Fibonacci"""

import datetime

""" RECURSIVE"""
""" O(n) = n^2 """
""" Up to 50 kill"""
def recursiveFibo(n):
    #print("Calculando Fibonacci de {}".format(n))
    if n <= 1:
        return n
    else:
        return recursiveFibo(n-1) + recursiveFibo(n-2)


"""MEMOIZACIÓN"""
""" Up to 1000 kill: most recent call last"""
""" O(n) = 2n | O(n) = n  <- Complegidad lineal pero con el problema de STACK"""
memo = [0, 1]
def memoizedFibo(n, memo):
    if (n < len(memo)):
        return memo[n]
    if (n <= 1):
        memo.append(n)
        return n
    else:
        result = memoizedFibo(n - 1, memo) + memoizedFibo(n - 2, memo)
        memo.append(result)
        #print(memo,len(memo))
        return result


""" Dinamic program (LINEAR) """
""" O(n) = n    <- Complegidad lineal. """
def linearFibo(n):
    memo = [0, 1]
    actual = 2
    while (actual <= n):
        memo.append(memo[actual - 2] + memo[actual - 1])
        actual += 1

    return memo[n]


def run():
    print("Welcome to Fibonacci Algorithms.")
    n = int(input("Enter a number: "))

    print("[RECURSIVE]")
    start = datetime.datetime.now()
    #result = recursiveFibo(n)
    result = 0
    end = datetime.datetime.now()
    print("Result: {}  \tTime: {}  X'( ".format(result,(end - start)))

    print("[MEMOIZED]")
    start = datetime.datetime.now()
    result = memoizedFibo(n,memo)
    end = datetime.datetime.now()
    print("Result: {}  \tTime: {}".format(result,(end - start)))
    
    print("[LINEAR - DINAMIC PROGRAM]")
    start = datetime.datetime.now()
    result = linearFibo(n)
    end = datetime.datetime.now()
    print("Result: {}  \tTime: {}".format(result,(end - start)))
    print("bye.")



if __name__ == "__main__":
    run()
