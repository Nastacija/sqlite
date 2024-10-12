from itertools import product

def read_seg(filename, encoding = 'UTF-8'):

    letters = "GBRY"
    nums = "1234"
    levels = [ch + num for num, ch in product(nums, letters)]
    level_codes = [2 ** i for i in range(len(levels))]

    level2code = {i: j for i, j in zip(levels, level_codes)}
    code2level = {j: i for i, j in zip(levels, level_codes)}

    fh = open(filename, 'r', encoding = encoding)
    lines = fh.readlines()
    start = 1
    fin = lines.index('[LABELS]\n')
    param_dict = {}
    labels = []
    for line in lines[start:fin]:
        line = line.strip()
        param_name, param_value = line.split('=')
        param_value = int(param_value)
        param_dict[param_name] = param_value
    for line in lines[fin + 1:]:
        line = line.strip()
        pos, level, alloph = line.split(',', maxsplit = 2)
        pos = int(pos) // param_dict['BYTE_PER_SAMPLE'] // param_dict['N_CHANNEL']
        level = code2level[int(level)]
        label = {
            'position': pos,
            'level': level,
            'name': alloph
        }
        labels.append(label)
    return param_dict, labels