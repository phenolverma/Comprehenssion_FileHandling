import csv

infile = open(r'./../Data/Employee.csv', 'r')
outfile = open(r'./../Data/Outfile_2_Col.csv', 'w')
read_csv = csv.reader(infile)
data = list(read_csv)
write_csv = csv.writer(outfile)
new_data = []

for each in data:
    new_data.append(each[1])
    new_data.append(each[3])
    write_csv.writerow(new_data)
    new_data = []

outfile.close()

