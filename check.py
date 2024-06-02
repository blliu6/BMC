import z3
from z3 import *
from aag import aag
from read_aag import read_aag


def get_var(var, pos):
    if (pos & 1) == 0:
        return var[pos // 2 - 1]
    else:
        return Not(var[pos // 2 - 1])


def check(example: aag, kk: int):  # 执行k轮
    # 第一轮
    x0 = [Bool(f'x{i + 1}') for i in range(example.n)]
    # 首先非门关系
    solver = Solver()

    for i, j in example.cache_list:
        solver.add(Not(get_var(x0, i)))
    # 处理与门关系
    for i, j, k in example.and_gate_list:
        solver.add(get_var(x0, i) == And(get_var(x0, j), get_var(x0, k)))

    for item in example.output_list:
        solver.push()
        solver.add(get_var(x0, item))

    var = [x0]
    for _ in range(kk):
        if solver.check() == z3.sat:
            print(f'k:{_}->sat')
            print(solver.model())
            break
        else:
            for item in example.output_list:
                solver.pop()
            var.append([Bool(f'x{i + 1 + (_ + 1) * example.n}') for i in range(example.n)])
            for v, w in example.cache_list:
                solver.add(get_var(var[-1], v) == get_var(var[-2], w))
            for i, j, k in example.and_gate_list:
                solver.add(get_var(var[-1], i) == And(get_var(var[-1], j), get_var(var[-1], k)))

            for item in example.output_list:
                solver.push()
                solver.add(get_var(var[-1], item))
            print(f'k:{_}->unsat')


if __name__ == '__main__':
    example = read_aag('./ex.aag')
    check(example, 10)
