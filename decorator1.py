__author__ = 'zhangxun'

def log(text):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print '%s %s(): ' % (text, func.__name__)
            return func(*args,**kwargs)
        return wrapper
    return decorator

@log('execute')
def now():
    print '2015/1/1'

now()
print "hello world"
