# Usage: 
# python varakozasi_graf.py "l1(B); l2(C); l3(D); l1(A); l2(B); l3(A); l4(C); u1(B); l2(D);" 

# Minden lépés után megjelenik a konzolon az aktuális eredmény.
# Gráf helyett listákkal vannak ábrázolva a nyilak.
# Pl. [1] -> [2, 3] == 1-ből 2-be és 3-ba vezet nyíl

from sys import argv

class Operation:
    def __init__(self, op_str):
        self.action = op_str[0].upper()            # [L]ock vagy [U]nlock
        self.num    = op_str[1]                    # 1, 2, ...
        self.var    = op_str.split('(')[1].upper() # A, B, C, D, ...
    def __repr__(self):
        return self.__str__()
    def __str__(self):
        return f'{self.action}{self.num}({self.var})'
    def conflicts(self, other):
        return self.var == other.var and \
            ((self.action == 'W' and other.action == 'W') or \
             (self.action == 'W' and other.action == 'R') or \
             (self.action == 'R' and other.action == 'W'))

T = [Operation(arg.strip()) for arg in argv[1].rstrip(';').split(';')]
Result = {}
for op in T:
    if op.num not in Result:
        Result[op.num] = []

Locked = {}

i = 0
while i < len(T):
    op = T[i]
    if op.action == 'L':
        if op.var not in Locked:
            Locked[op.var] = (op.num, i)
        else:
            if Locked[op.var][0] not in Result[op.num]:
                Result[op.num] += Locked[op.var][0]
    elif op.action == 'U' and op.var in Locked:
        for j in range(Locked[op.var][1], i):
            op2 = T[j]
            if op2.var == op.var and op.num in Result[op2.num]:
                Result[op2.num].remove(op.num)
        del Locked[op.var]
    print(f'#{i + 1}')
    for key in sorted(Result): print(f'[{key}] -> {", ".join(Result[key])}')
    print()
    i+=1
