a = [1,2]
b = 3

def fun(x):
    if isinstance(x, int):
        x = x + 1
    else:
        x = x + [1]
fun(b)
fun(a)

print(a)
print(b)