import sys
a = bytes('hello'.encode(encoding='utf-8'))
print(a.__sizeof__())

b = list(range(5))  # 28位 4字节
for data in b:
    print(id(data))
