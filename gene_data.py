f = open(r"C:\Users\LENOVO\PycharmProjects\amity\Assignment\gene.txt", "r")
x = open("result_gene_property.txt", "w")

def read_sequence(f):
    x = ''
    for i in f.readlines():
        x += "".join(i.replace("\n", ""))
    return x

def complement(b):
    temp = []
    complementary = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    for x in b:
        temp.append(complementary[x])
    return(''.join(temp))

def compute_GC(b):
    return(((b.count("C") + b.count("G")) / float(len(b)) * 100))

def seq_length(b):
    return(b.count("A") + b.count("T") + b.count("G") + b.count("C"))

a = f.readline()
b = read_sequence(f)

x.write("Header file: %s\n" % a.replace("\n", ""))
x.write("Complementary strand: %s\n" % complement(b))
x.write("GC percentage is: %s\n" % '%.2f'%compute_GC(b))
x.write("Length of the sequence is: %s" % seq_length(b))

x.close()
f.close()