from collections import namedtuple

OpInfo = namedtuple('OpInfo', 'prec assoc')
L, R = 'Left Right'.split()
 
ops = {
 '^': OpInfo(prec=4, assoc=R),
 '*': OpInfo(prec=3, assoc=L),
 '/': OpInfo(prec=3, assoc=L),
 '+': OpInfo(prec=2, assoc=L),
 '|': OpInfo(prec=1, assoc=L),
 '(': OpInfo(prec=9, assoc=L),
 ')': OpInfo(prec=0, assoc=L),
 }
 
NUM, LPAREN, RPAREN = 'NUMBER ( )'.split()
 
def get_input(inp = None):
    tokens = inp.split()
    tokenvals = []
    for token in tokens:
        if token in ops:
            tokenvals.append((token, ops[token]))
        else:    
            tokenvals.append((NUM, token))
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
    while stack:
        t2, (p2, a2) = stack[-1]
        stack.pop()
        outq.append(t2)
        table.append( (' '.join(outq), ' '.join(s[0] for s in stack)) )
    return table[-1][0]