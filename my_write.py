outfile = open(r'./../Data/write.txt', 'a')
outfile.write('I am Phenol Verma\n')
outfile.write('I am Phenol Verma\n')
outfile.write('I am Phenol Verma\n')
outfile.flush()
read_file = open(r'./../Data/write.txt', 'r')
print(read_file.read())