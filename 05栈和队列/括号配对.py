from list_stack import Stack as stack


class MatchError():
    pass



def check_parents(text):
    """检查其括号是否正确配对"""
    parents = "()[]{}"
    open_parents = "([{"
    parents_dict = {"(": ")", "[": "]", "{": "}"}
    parents_stack = stack()
    flag = True
    comment_flag = False

    for ele in text:
        if ele == "#":
            comment_flag = True
        if comment_flag == True and ele == "\n":
            comment_flag = False

        if not comment_flag:
            if ele in open_parents:
                parents_stack.push(ele)  # 开括号压栈
            elif ele in parents:
                if ele == parents_dict[parents_stack.pop()]:  # match
                    pass
                else:
                    flag = False
                    print("match_error")
                    break

    if flag and parents_stack.is_empty():
        print("match_ok")
    else:
        print("缺少括号")


check_parents("[hello(){}]#[[]]{\n")