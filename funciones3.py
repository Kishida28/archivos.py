def fibonacci(num):
    a, b = 0, 1
    while a < num:
        print(a)
        a, b = b, a + b

fibonacci(10)        
