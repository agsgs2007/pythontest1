__author__ = 'zhangxun'

name = ['MIKE','Lisa','adam']
def Uppercase(x):
    return '%s%s' % (x[0].upper(), x[1:].lower())

print map(Uppercase, name)

def is_odd(n):
    return n%2==1
print filter(is_odd, [1,2,3,4,5,6,7])

def is_susu(n):
    if n<=1:
        return False
    i=2
    while i*i <=n:
        if n%i ==0:
            return False
        i +=1
    return True

print filter(is_susu, range(1,101))