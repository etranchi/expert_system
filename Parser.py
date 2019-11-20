from collections import namedtuple

OpInfo = namedtuple('OpInfo', 'prec assoc')
L, R = 'Left Right'.split()

ops = {
 '^': OpInfo(prec=4, assoc=R),
 '+': OpInfo(prec=2, assoc=L),
 '|': OpInfo(prec=1, assoc=L),
 '(': OpInfo(prec=9, assoc=L),
 ')': OpInfo(prec=0, assoc=L),
 }

NUM, LPAREN, RPAREN = 'NUMBER ( )'.split()

def get_input(inp = None):
    inp = inp.replace(" ", "")
    inp = inp.replace("", " ")
    if inp.count("(") > 1 or inp.count(")") > 1 or not inp.count("(") == inp.count(")"):
        raise Exception
    while inp[1] == "(" and inp[-2] == ")":
        inp = inp[2:]
        inp = inp[:-2]
    tokens = inp.split()
    tokenvals = []
    excl = 0
    n_op = 0
    n_fact = 0
    for t in tokens:
        if t == "!":
            if not excl:
                excl = 1
            else:
                raise Exception
        elif t.isalpha():
            n_fact += 1
            excl = 0
        else:
            if excl:
                raise Exception
            elif t not in ops:
                raise Exception
    if excl:
        raise Exception
    for token in tokens:
        if token in ops:
            if not token == '(' and not token == ')':
                n_op += 1
            tokenvals.append((token, ops[token]))
        else:
            tokenvals.append((NUM, token))
    if not n_fact - 1 == n_op:
        raise Exception
    return tokenvals

def shunting(tokenvals):
    outq, stack = [], []
    table = []
    tokenvals = get_input(tokenvals)
    for token, val in tokenvals:
        if token is NUM:
            outq.append(val)
        elif token in ops:
            t1, (p1, a1) = token, val
            while stack:
                t2, (p2, a2) = stack[-1]
                a2 = a2
                if (a1 == L and p1 <= p2) or (a1 == R and p1 < p2):
                    if t1 != RPAREN:
                        if t2 != LPAREN:
                            stack.pop()
                            outq.append(t2)
                        else:
                            break
                    else:
                        if t2 != LPAREN:
                            stack.pop()
                            outq.append(t2)
                        else:
                            stack.pop()
                            break
                else:
                    break
            if t1 != RPAREN:
                stack.append((token, val))
    if len(stack):
        while stack:
            t2, (p2, a2) = stack[-1]
            stack.pop()
            outq.append(t2)
            table.append( (' '.join(outq), ' '.join(s[0] for s in stack)) )
    else :
        return str(outq[0])
    res = table[-1][0]
    for c in res:
        if c == '(' or c == ')':
            raise Exception
    return res.replace(" ", "")