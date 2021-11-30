# Usage: 
# python megelozesi_graf.py "R1(A); R3(B); R4(C); R1(B); R2(A); W2(A); W2(B); W3(C); R4(A); W4(D);" 

# Minden lépés után megjelenik a konzolon az aktuális eredmény.
# Gráf helyett listákkal vannak ábrázolva a nyilak.
# Pl. [1] -> [2, 3] == 1-ből 2-be és 3-ba vezet nyíl

from sys import argv

class Operation:
    def __init__(self, op_str):
        self.action = op_str[0].upper()            # [R]ead vagy [W]rite
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

for i in range(len(T)):
    for j in range(i+1, len(T)):
        if  T[i].num != T[j].num and T[i].conflicts(T[j]) and T[j].num not in Result[T[i].num]:
            Result[T[i].num] += T[j].num

for key in sorted(Result): print(f'[{key}] -> {", ".join(Result[key])}')