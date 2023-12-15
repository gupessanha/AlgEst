def prefixa_p_infixa_posfixa(exp, index=0):
    if exp[index].isdigit():
        return exp[index], exp[index], index + 1

    op = exp[index]
    index += 1

    left_infixa, left_posfixa, index = prefixa_p_infixa_posfixa(exp, index)
    right_infixa, right_posfixa, index = prefixa_p_infixa_posfixa(exp, index)

    infixa = "(" + left_infixa + op + right_infixa + ")"
    posfixa = left_posfixa + right_posfixa + op

    return infixa, posfixa, index



exp = ['*', '+', '2', '3', '4']
infixa, posfixa, _ = prefixa_p_infixa_posfixa(exp)
print('Expressão Infixa:', infixa)
print('Expressão Posfixa:', posfixa)
