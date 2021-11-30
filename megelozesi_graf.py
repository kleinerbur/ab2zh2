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