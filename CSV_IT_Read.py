import csv

infile = open(r'./../Data/Employee.csv', 'r')
outfile = open(r'./../Data/Outfile.csv', 'w')
read_csv = csv.reader(infile)
data = list(read_csv)
write_csv = csv.writer(outfile)
row_count = 0

for each in data:
    if row_count == 0:
        write_csv.writerow((data[row_count]))
    if each[3] == 'IT':
        write_csv.writerow(data[row_count])
    row_count += 1

outfile.close()

