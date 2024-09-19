def add_everything_up(a,b):
    try:
        return a+b
    except TypeError as exte:
        return str(a)+str(b)
    
print(add_everything_up('sd',5))
print(add_everything_up(5,1.234))
print(add_everything_up(2.345,'float'))
print(add_everything_up(1+3j,2-5j))
