def counter(n):
    i = 0
    while i < n:
        yield(i)
        i += 1
        
for x in counter(3):
    print(x)