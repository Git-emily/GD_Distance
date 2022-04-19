def foo(n):
    i = 2
    def bar(i):
         n += i
         return n
    return bar

if __name__ == '__main__':
    test = foo(3)    
    print(test)