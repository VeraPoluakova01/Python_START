"""
Напишите программу вычисления арифметического выражения заданного строкой.
Используйте операции +,-,/,*. приоритет операций стандартный.
По возможности реализуйте использования скобок, меняющих приоритет операций.

Ввод: значение типа <str>
Вывод: значение числового типа данных
"""
# message = '1 + 2 + 5 + 8'
# # if message.startswith("!число"):
# a, symbol, b = message.split()
# if symbol == '+':
#     print(float(a) + float(b))


def calk(exp: str) -> str:
    if isdigit(exp):
        return exp

    if "(" in exp:
        ind_s, ind_f = find_bracket(exp)
        if ind_s != ind_f:
            exp = exp[0:ind_s] + calk(exp[ind_s + 1:ind_f]) + exp[ind_f + 1:]
            exp = calk(exp)

    if "*" in exp or "/" in exp:
        ind_s, ind_f, ind_o = find_expression(exp, ["*", "/"])
        if exp[ind_o] == "*":
            exp = (exp[0:ind_s] + str(float(exp[ind_s:ind_o]) *
                   float(exp[ind_o + 1:ind_f + 1])) + exp[ind_f + 1:])
            exp = calk(exp)
        elif exp[ind_o] == "/":
            exp = exp[0:ind_s] + \
                str(float(exp[ind_s:ind_o]) / float(exp[ind_o + 1:ind_f + 1])) + \
                exp[ind_f + 1:]
            exp = calk(exp)

    if isdigit(exp):
        return exp

    if "+" in exp or "-" in exp:
        ind_s, ind_f, ind_o = find_expression(exp, ["+", "-"])
        if exp[ind_o] == "+":
            exp = (exp[0:ind_s] + str(float(exp[ind_s:ind_o]) +
                   float(exp[ind_o + 1:ind_f + 1])) + exp[ind_f + 1:])
            exp = calk(exp)
        elif exp[ind_o] == "-":
            exp = exp[0:ind_s] + \
                str(float(exp[ind_s:ind_o]) - float(exp[ind_o + 1:ind_f + 1])) + \
                exp[ind_f + 1:]
            exp = calk(exp)

    return exp


def calculator(data: str) -> float:
    return float(calk(data))


def isdigit(data):
    try:
        float(data)
    except ValueError:
        return False
    return True


def find_expression(data: str, search_operand: list):
    ind_s = 0
    ind_f = 0
    ind_o = 0
    operands_fool = ["+", "-", "/", "*"]
    operands = ["+", "-", "/", "*"]
    for op in search_operand:
        operands.remove(op)
    found = False

    for i, sym in enumerate(data):
        if i == 0 and sym == "-":
            continue
        if not found and sym in operands:
            ind_s = i + 1
        elif found and sym in operands_fool:
            ind_f = i - 1
            return ind_s, ind_f, ind_o

        elif sym in search_operand:
            found = True
            ind_o = i
            ind_f = len(data) - 1

    return ind_s, ind_f, ind_o


def find_bracket(data: str):
    ind_s = 0
    ind_f = 0
    for i, sym in enumerate(data):
        if sym == "(":
            ind_s = i
        elif sym == ")":
            ind_f = i
            return ind_s, ind_f
    return ind_s, ind_f


if __name__ == '__main__':
    exp = input('введите выражение ')
    print(calculator(exp))
