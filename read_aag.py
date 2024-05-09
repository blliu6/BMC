from aag import aag


def read_aag(filename) -> aag:
    with open(filename, 'r') as f:
        header = f.readline().strip().split(' ')
        header = [int(header[i + 1]) for i in range(len(header) - 1)]
        AAG = aag(*header)
        for i in range(AAG.input):
            line = int(f.readline().strip())
            AAG.input_list.append(line)

        for i in range(AAG.cache):
            line = f.readline().strip().split(' ')
            line = [int(item) for item in line]
            AAG.cache_list.append(line)

        for i in range(AAG.output):
            line = int(f.readline().strip())
            AAG.output_list.append(line)

        for i in range(AAG.and_gate):
            line = f.readline().strip().split(' ')
            line = [int(item) for item in line]
            AAG.and_gate_list.append(line)

        return AAG


if __name__ == '__main__':
    aag = read_aag('./ex.aag')
    aag.show()
