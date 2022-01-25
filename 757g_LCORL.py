from collections import defaultdict
f_out = open('757JD.lcorl.txt', 'w')

with open('jindodog_input_covar.covar', 'r') as f2:
    pheno = defaultdict(list)
    for lines in f2.readlines()[1:]:
        data2 = lines.strip().split('\t')
        if data2[5].startswith('-9') + data2[-1].startswith('-9'): continue
        pheno[data2[0]] = (float(data2[5]) + float(data2[-1])) / 2
#    for key, value in pheno.items():
#        if data[-1] == "A A" and data[0] == key:
#            f_out.write(f"{}\n")
#        if data[-1] == "A G" and data[0] == key:
#            f_out.write(f"{data[0]}\t{round(value, 2)}\t{data[-1]}\n")
#        if data[-1] == "G G" and data[0] == key:
#            f_out.write(f"{data[0]}\t{round(value, 2)}\t{data[-1]}\n")
    with open('757JD_LCORL.ped', 'r') as f:
        genotype = {}
        for line in f.readlines():
            data = line.strip().split('\t')
            genotype[data[-1]] = data[0]
            
