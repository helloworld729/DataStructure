def bintree(data, left, right):
    return [data, left, right]

def is_empty_bintree(bin_tree):
    return len(bin_tree) == 0

def root(bin_tree):
    return bin_tree[0]

def left(bin_tree):
    return bin_tree[1]

def right(bin_tree):
    return bin_tree[2]

def set_root(bin_tree, data):
    bin_tree[0] = data

def set_left(bin_tree, data):
    bin_tree[1] = data

def set_right(bin_tree, data):
    bin_tree[2] = data
# ########################### 表达式应用 ##########################
def make_sum(a, b):
    return ['+', a, b]
def make_diff(a, b):
    return ['-', a, b]
def make_prod(a, b):
    return ['*', a, b]
def make_div(a, b):
    return ['/', a, b]
def is_basic_exp(e):
    return not isinstance(e, list)
def is_num(n):
    return isinstance(n, int) or isinstance(n, float) or isinstance(n, complex)
def eval_exp(e):  # 递归
    if is_basic_exp(e): # 终止条件
        return e
    op, a, b = e[0], eval_exp(e[1]), eval_exp(e[2])  # 递归表达式
    if op == '+':  # 每次递归返回后的操作
        return a + b
    if op == '-':
        return a - b
    if op == '/':
        return a / b
    if op == '*':
        return a * b

t = bintree('*',3, ['+', 2,5])
print(t)
r = make_sum(t, ['/', 6, 2])
print(r)
print(eval_exp(r))