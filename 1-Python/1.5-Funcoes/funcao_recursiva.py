# fatorial
# 5! = 5*4*3*2*1 = 120

def fatorial(n):
    if n == 1:
        return 1
    return n * fatorial(n-1)

print(fatorial(5))