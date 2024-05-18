def caching_fibonacci():
    cache = {}

    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        
        # check numbers in cache
        if n in cache:
            return cache[n]

        # calculate number in recursion and save in cache
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci

fibonacci = caching_fibonacci()
print(fibonacci(10))  #55
print(fibonacci(15))  #610
