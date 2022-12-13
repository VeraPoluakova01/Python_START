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


def find(exp, sech_operand):
    ind_start = 0
    ind_finish = 0
    ind_oper = 0
    operands_full = ['*', '/', '-', '+']
    operands = ['*', '/', '-', '+']
    for op in sech_operand:
        operands.remove(op)
    found = False
    for i, sim in enumerate(exp):
        if i == 0 and sim == '-':
            continue
        if not found and sim in operands:
            ind_start = i + 1
        elif found and sim in operands_full:
            ind_finish = i - 1
            return ind_start, ind_finish, ind_oper
        elif sim in sech_operand:
            found = True
            ind_oper = i
            ind_finish = len(exp) - 1
    return ind_start, ind_finish, ind_oper


def calk(exp):
    if '*' in exp or '/' in exp:
        ind_s, ind_f, ind_o = find(exp, ['*', '/'])
        if exp[ind_o] == '*':
            exp = exp[0:ind_s] + str(float(exp[ind_s:ind_o])
                                     * float(exp[ind_o + 1:ind_f + 1])) + exp[ind_f+1:]
            exp = calk(exp)
        elif exp[ind_o] == '/':
            exp = exp[0:ind_s] + str(float(exp[ind_s:ind_o]) /
                                     float(exp[ind_o + 1:ind_f + 1])) + exp[ind_f+1:]
            exp = calk(exp)

    if '+' in exp or '-' in exp:
        ind_s, ind_f, ind_o = find(exp, ['+', '-'])
        if exp[ind_o] == '+':
            exp = exp[0:ind_s] + str(float(exp[ind_s:ind_o]) +
                                     float(exp[ind_o + 1:ind_f + 1])) + exp[ind_f+1:]
            exp = calk(exp)
        elif exp[ind_o] == '-':
            exp = exp[0:ind_s] + str(float(exp[ind_s:ind_o]) -
                                     float(exp[ind_o + 1:ind_f + 1])) + exp[ind_f+1:]
            exp = calk(exp)
    return exp

if __name__ == '__main__':
    exp = '3*4/2'
    print(calk(exp))

   