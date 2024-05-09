class aag:
    def __init__(self, n, input_n, cache, output, and_gate):
        self.n = n  # 变量个数
        self.input = input_n  # 输入个数
        self.cache = cache
        self.output = output
        self.and_gate = and_gate
        self.input_list = []
        self.output_list = []
        self.cache_list = []
        self.and_gate_list = []

    def show(self):
        print(f'输出：{self.input_list}')
        print(f'缓存：{self.cache_list}')
        print(f'输出：{self.output_list}')
        print(f'与门：{self.and_gate_list}')
