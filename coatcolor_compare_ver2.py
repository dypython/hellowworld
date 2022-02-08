from collections import defaultdict
f_out = open('Y+All.chr21_2.txt', 'w')
with open('Y+All.chr21_2.ped', 'r') as f:
    for line in f.readlines():
        data = line.strip().split('\t')
        with open('pheno_coatcolor_python.txt', 'r') as f2:
            colors = defaultdict(list)
            for lines in f2.readlines():
                data2 = lines.strip().split('\t')
                colors[data2[1]].append(lines)
            for key, value in colors.items():
                if data[0] in key:
                    for a in value:
                        data3 = a.strip()
                        f_out.write(f"{data[-1]}\t{data3}\n")
