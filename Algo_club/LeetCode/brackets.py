# Задача номер 20(Valid Parentheses) на сайте LeetCode.
# Задача про коректную скобковую запись.
# Если запись корректна то возвращает True, иначе False.


def cor(s):
    ans = []
    lst = list(s)
    v = ('()', '{}', '[]')
    for i in lst:
        if not ans:
            ans.append(i)
        else:
            if ans[-1] + i in v:
                ans.pop()
            else:
                ans.append(i)

    return False if ans else True
