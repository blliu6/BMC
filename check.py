from dreal import *
from aag import aag
from read_aag import read_aag


def check(example: aag, k: int):  # 执行k轮
    # 第一轮
    episode = 0
    x0 = [Variable(f'x{i + 1}', Variable.Binary) for i in range(example.n * 2)]
    # 首先非门关系
    con = And()
    i = 0
    while i < example.n * 2:
        con = And(con, x0[i] == Not(x0[i + 1]))
        i = i + 2



if __name__ == '__main__':
    example = read_aag('./ex.aag')
